from rest_framework import serializers
from .models import Items, auctons


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"


class auctonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = auctons
        fields = "__all__"
