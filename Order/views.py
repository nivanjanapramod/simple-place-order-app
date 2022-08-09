from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomerSerializer, OrderSerializer
from .models import Customer, Order
import datetime

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CapacityView(APIView):
    def get(self, request):
        Max_capacity = 1000
        left_amount = 0
        orders = Order.objects.filter(ordered_on__date=datetime.date.today())
        for order in orders:
            left_amount+=order.amount
    
        data = Max_capacity - left_amount
        return Response(data=data)