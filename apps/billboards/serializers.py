from rest_framework import serializers

from .models import Billboard


class BillboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billboard
        fields = [
            'owner',
            'image',
            'size',
            'location',
            'available_date',
            'target_audience',
            'created_at',
        ]
