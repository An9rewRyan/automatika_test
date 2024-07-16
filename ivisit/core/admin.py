from django.contrib import admin
from .models import Worker, TradePoint, Visit


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number')
    search_fields = ('name',)


@admin.register(TradePoint)
class TradePointAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'worker')
    search_fields = ('name',)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'trade_point', 'worker', 'latitude', 'longitude')
    search_fields = ('worker__name', 'trade_point__name')
