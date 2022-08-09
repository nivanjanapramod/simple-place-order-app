from django.contrib import admin
from django.urls import path

from .views import CustomerViewSet, OrderViewSet, CapacityView

order_add = OrderViewSet.as_view({'post':'create'})
order_update = OrderViewSet.as_view({'put': 'update'})
update_status = OrderViewSet.as_view({'patch': 'partial_update',})
delete_order = OrderViewSet.as_view({'delete': 'destroy'})
customer_add = CustomerViewSet.as_view({'post':'create'})

urlpatterns = [
    path('add/', order_add, name='order_add'),
    path('update/<int:pk>/', order_update, name='order_update'),
    path('update_status/<int:pk>/', update_status, name='update_status'),
    path('delete/<int:pk>/', delete_order, name='delete_order'),
    path('create-account/', customer_add, name='customer_add'),
    path('checkCapacity/', CapacityView.as_view()),
]
