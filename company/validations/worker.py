from rest_framework import serializers

def validate_firstName(value):
        if not value:
            raise serializers.ValidationError("Name is required")
        return value

def validate_secondName(value):
    if not value:
        raise serializers.ValidationError("Second name is required")
    return value

def validate_description(self, value):
    if len(value) > 256:
        raise serializers.ValidationError("Max description length - 256")
    return value

def validate_position(value):
    valid_positions = ["Tl", "Sd1", "Sd2", "Sd3", "Sd4"]
    if value not in valid_positions:
        raise serializers.ValidationError(
            f"Posititon must be oneof: {', '.join(valid_positions)}."
        )
    return value