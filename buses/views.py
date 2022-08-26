from ctypes.wintypes import PHANDLE
from multiprocessing import context
from django.shortcuts import render
from buses.models import Bus,Seat,Seat_details
from django.contrib.auth.models import auth
from datetime import datetime

# Create your views here.
from django.shortcuts import render,redirect
from django.http.response import HttpResponseRedirect
from django.contrib.auth import logout 

def index(request):
    return render(request,'site/index.html')

def seatbook(request,pk=None):
    context = {}

    if pk is not None:
        bus_obj = Bus.objects.get(id=pk)
        if bus_obj.seat.exists():
            
            print('ok')
        elif Seat.objects.filter().exists():
            dumy_seat = Seat.objects.all().order_by('seat_no')
            all_seat = []
            for one_dumy_seat in dumy_seat:
                createing_seat = Seat_details.objects.create(seat_no=one_dumy_seat.seat_no)
                bus_obj.seat
                all_seat.append(createing_seat)
            bus_obj.seat.add(*all_seat)
            

    if request.method == 'POST':
        seat_selected = []
        total_price = 0

        seat_id_list = request.POST.getlist('seat_choise')
        for seat_id in seat_id_list:
            obj = Seat_details.objects.get(id=int(seat_id))
        #     obj.seat_available = False
        #     obj.seta_book_by = request.user
        #     obj.seat_booked_time = datetime.now()
        #     obj.save()
            seat_selected.append(obj)
            total_price += bus_obj.price
        #     print(seat_id)
        return render (request,'site/busbook.html',{'seat_selected':seat_selected,'bus_data':bus_obj,'total_price':total_price})
        

        # Seat_details
        # print(request.POST.getlist('seat_choise'))
    context['bus_data'] = bus_obj
    return render(request,'site/seatbook.html',context)

def busbook(request):
    context = {}
    if request.method == 'POST':
        destination_from = request.POST['from']
        context['data_from'] = destination_from
        destination_to = request.POST['to']
        context['data_to'] = destination_to
        bus_date = request.POST['booking_date']
        context['data_booking_date'] = bus_date
        buslist = Bus.objects.filter(destination_from=destination_from, destination_to=destination_to,date=bus_date)
        context={
            'buslist':buslist
        }
     
    return render(request,'site/bookingform.html',context)


def bookingticket(request):
    return render(request,'site/busbook.html')


def confirmticket(request):
    if request.method == 'POST':
        seat_selected = []
        total_price = 0
        bus_obj = Bus.objects.get(id = int(request.POST.get('bus_id')))
        seat_id_list = request.POST.getlist('seat_choise')
        print(len(seat_id_list))
        passenger_names = request.POST.getlist('name')
        for i in range(len(seat_id_list)):
            print(i)
            print(seat_id_list[i])
            obj = Seat_details.objects.get(id=int(seat_id_list[i]))
            obj.seat_available = False
            obj.seta_book_by = request.user
            obj.passenger_name = passenger_names[i]
            obj.seat_booked_time = datetime.now()
            obj.save()
            seat_selected.append(obj)
            total_price += bus_obj.price
    
    return render(request,'site/success.html')