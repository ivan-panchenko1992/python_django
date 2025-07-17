from rest_framework import serializers
from .models import Item
from .validations.worker import validate_firstName, validate_secondName, validate_description, validate_position
import re



class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'firstName', 'secondName', 'position', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_firstName(self, value):
        return validate_firstName(value)

    def validate_secondName(self, value):
        return validate_secondName(value)

    def validate_description(self, value):
        return validate_description(value)

    def validate_position(self, value):
        return validate_position(value)
class ItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['description', 'position']
        read_only_fields = []

    def validate_description(self, value):
        return validate_description(value)

    def validate_position(self, value):
        return validate_position(value)

