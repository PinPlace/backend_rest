from rest_framework import serializers
from pins.models import Pins, Lists

# Pin & List Serializers

class PinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pins
        fields = '__all__'

class ListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lists
        fields = '__all__'