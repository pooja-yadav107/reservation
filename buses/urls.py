from django.urls import path
from buses import views


urlpatterns = [
    path('', views.index, name='index'),
    path('bookticket/',views.busbook, name='bookticket'),
    path('seatbook/<int:pk>/',views.seatbook, name='seatbook'),
    path('bookingticket/',views.bookingticket, name='bookingticket'),
    path('confirmticket/',views.confirmticket, name='confirmticket'),
 
]