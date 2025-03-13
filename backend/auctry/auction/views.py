from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemsSerializer
from .models import Items, auctons
from accounts.views import add_auctons_func, deduct_auctons_func
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

class All_items(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.headers)  # ✅ See if Cookie is even sent
        print(request.COOKIES)
        serializer = ItemsSerializer(Items.objects.all(), many=True)
        data = serializer.data
        return Response(data)


class Selling_items(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ItemsSerializer(
            Items.objects.filter(seller=request.user), many=True
        )
        data = serializer.data
        return Response(data)


class post_item(APIView):

    def post(self, request):
        data = request.data
        user = User.objects.get(username=request.user)

        data["seller"] = user.id
        data["last_price"] = data["initial_price"]
        serializer = ItemsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class Bid(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        bidder = User.objects.get(username=request.user)
        item = Items.objects.get(pk=request.data["item_id"])
        bid = request.data["bid"]
        item_init_price = item.initial_price
        item_step_price = item.step_price
        item_last_price =

        if (bid - (item_last_price + item_step_price)) > 0 and bid > item_last_price:
            deducted = deduct_auctons_func(bidder, bid)
            if deducted:
                item.last_price = bid

                if item.last_bidder_1 != bidder:
                    item.last_bidder_3 = item.last_bidder_2
                    item.last_bidder_2 = item.last_bidder_1
                    item.last_bidder_1 = bidder
                item.save()
                return Response(
                    f"{bidder.username} Bidded on {item.name} succesfully at {bid}",
                    status=200,
                )
            else:
                return Response("not enough funds")

        return Response(
            {"message": "non-valid bid"},
            status=400,
        )

def check_auth(request):
    return JsonResponse({"user": str(request.user)})