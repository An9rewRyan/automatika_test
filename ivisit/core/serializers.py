from rest_framework import serializers
from .models import Worker, TradePoint, Visit
from django.utils import timezone
import pytz


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'name', 'phone_number']


class TradePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradePoint
        fields = ['id', 'name']


class VisitSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField()

    class Meta:
        model = Visit
        fields = ['id', 'timestamp']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        moscow_tz = pytz.timezone('Europe/Moscow')
        timestamp = instance.timestamp.astimezone(moscow_tz)
        representation['timestamp'] = timestamp.isoformat()
        return representation
