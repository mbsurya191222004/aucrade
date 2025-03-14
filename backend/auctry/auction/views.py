from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemsSerializer, BidsSerializer
from .models import Items, auctons, Bids
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
        serializer = ItemsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class Bid(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        item = Items.objects.get(pk=data["item_Id"])
        init_price = item.initial_price
        step_price = item.step_price
        data["bidder"] = (User.objects.get(username=request.user)).id
        serializer = BidsSerializer(data=data)
        all_bids = (
            Bids.objects.filter(item_Id=data["item_Id"]).order_by("-bid").values()
        )
        if serializer.is_valid():
            if all_bids:
                if (
                    all_bids[0]["bid"] < data["bid"]
                    and data["bid"] > (init_price + step_price)
                    and ((data["bid"] - init_price) % step_price == 0)
                ):
                    serializer.save()
                    return Response(serializer.data, status=200)
                return Response(
                    {
                        "message": "bid lower than the highest or not according to step price"
                    },
                    status=400,
                )
            elif data["bid"] >= (init_price + step_price) and (
                (data["bid"] - init_price) % step_price == 0
            ):
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response({"message": "invalid bid"}, status=400)
        return Response(serializer.errors, status=400)


def check_auth(request):
    return JsonResponse({"user": str(request.user)})
