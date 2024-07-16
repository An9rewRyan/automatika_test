from django.urls import path
from .views import TradePointListView, VisitCreateView

urlpatterns = [
    path('points/', TradePointListView.as_view(), name='trade-point-list'),
    path('visits/', VisitCreateView.as_view(), name='visit-create'),
]
