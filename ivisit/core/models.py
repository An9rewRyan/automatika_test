from django.db import models
from django.db import models
from django.utils import timezone
import pytz


class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True


class TradePoint(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Visit(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    trade_point = models.ForeignKey(TradePoint, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def save(self, *args, **kwargs):
        moscow_tz = pytz.timezone('Europe/Moscow')
        self.timestamp = timezone.now().astimezone(moscow_tz)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Visit by {self.worker.name} at {self.trade_point.name} on {self.timestamp}'
