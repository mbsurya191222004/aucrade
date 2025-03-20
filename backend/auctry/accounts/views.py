from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from django.http import JsonResponse
from django.middleware.csrf import get_token
import jwt
from rest_framework_simplejwt.tokens import AccessToken
from auction.models import auctons


def add_auctons_func(user, amount):
    row = auctons.objects.get(pk=user.id)
    row.amount += amount
    row.save()
    return {"credited": {amount}, "current": {row.amount}}


def deduct_auctons_func(user, amount):
    row = auctons.objects.get(pk=user.id)
    if (row.amount - amount) >= 0:
        row.amount -= amount
        row.save()
        return {"debited": {amount}, "current": {row.amount}}
    return False


class add_auctons(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        amount = request.data["amount"]
        user = User.objects.get(username=request.user)
        if User:
            response = add_auctons_func(user, amount)
            return Response(response, status=200)
        return Response(status=404)


class deduct_auctons(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        amount = request.data["amount"]
        user = User.objects.get(username=request.user)
        if User:
            response = deduct_auctons_func(user, amount)
            return Response(response, status=200)
        return Response(status=404)


class login(APIView):

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(username=username, password=password)
        if user:
            # Generate JWT
            jwt_token = AccessToken.for_user(user)

            # Create response & set HttpOnly cookie
            response = Response({"message": "Login successful"})
            response.set_cookie(
                key="jwt",
                value=jwt_token,
                httponly=True,
                secure=True,  # Set True in production (HTTPS)
                samesite="None",  # Change to "Strict" if needed
                path="/",  # Prevents CSRF attacks
            )

            return response

        return Response({"error": "Invalid credentials"}, status=400)


class Sign_up(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            username = serializer.data["username"]
            return Response(
                {
                    "message": f"welcome {username} ",  # why here error?
                },
                status=200,
            )
        return Response(
            serializer.errors,
            status=400,
        )
