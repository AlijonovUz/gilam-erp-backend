from rest_framework import serializers

from apps.base.serializers import BaseModelSerializer

from ..models import Design


class DesignSerializer(BaseModelSerializer):
    """Gilam dizayni uchun serializer — sifat nested qaytariladi."""

    status = serializers.BooleanField(source="is_active", read_only=True)

    class Meta:
        model = Design
        fields = [
            "id",
            "quality",
            "name",
            "description",
            "status",
            "created_at",
            "updated_at",
        ]
        related_fields = {"quality": {"fields": ["id", "name"]}}
