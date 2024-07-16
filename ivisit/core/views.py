from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TradePoint, Visit
from .serializers import TradePointSerializer, VisitSerializer
from .authentication import PhoneAuthentication


class TradePointListView(APIView):
    authentication_classes = [PhoneAuthentication]

    def get(self, request, format=None):
        worker = request.user
        trade_points = TradePoint.objects.filter(worker=worker)
        if not trade_points.exists():
            return Response({'error': 'No trade points found for this worker'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TradePointSerializer(trade_points, many=True)
        return Response(serializer.data)


class VisitCreateView(APIView):
    authentication_classes = [PhoneAuthentication]

    def post(self, request, format=None):
        worker = request.user
        trade_point_id = request.data.get('trade_point_id')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        try:
            trade_point = TradePoint.objects.get(id=trade_point_id, worker=worker)
        except TradePoint.DoesNotExist:
            return Response({'error': 'Trade point not found or not associated with this worker'},
                            status=status.HTTP_404_NOT_FOUND)

        visit = Visit.objects.create(
            trade_point=trade_point,
            worker=worker,
            latitude=latitude,
            longitude=longitude
        )
        serializer = VisitSerializer(visit)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
