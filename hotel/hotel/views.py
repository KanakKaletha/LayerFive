from django.http import HttpResponseForbidden
from django.db import connection
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from booking.models import Room, Booking
from .backend import authenticate

def index(request):
    # check if the user is authenticated
    if not authenticate(request):
        return HttpResponseForbidden('You must provide a valid API key to access this view')

    return render(request, 'index.html')

########################### BY USING SQL QUERIES AS MENTIONED IN ASSIGNMENT ##############################
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def room_count_by_category(request, date=None):
    # check if the user is authenticated
    if not authenticate(request):
        return HttpResponseForbidden('You must provide a valid API key to access this view')

    if date:
        with connection.cursor() as cursor:
            query = """
                SELECT category, COUNT(category) as count
                FROM booking_room
                INNER JOIN booking_booking
                ON booking_room.room_id = booking_booking.room_id_id
                WHERE available = true
                AND start_date <= %s
                AND end_date >= %s
                GROUP BY category
            """
            cursor.execute(query, [date, date])
            rooms = dictfetchall(cursor)
            print(rooms)
    else:
        rooms = []
    return render(request, 'room_count_by_category.html', {'rooms': rooms})

@require_POST
def room_count_by_category_submit(request):
    # check if the user is authenticated
    if not authenticate(request):
        return HttpResponseForbidden('You must provide a valid API key to access this view')

    date = request.POST.get('date')
    return redirect('room_count_by_category', date=date)

def room_count_by_category_range(request, start_date=None, end_date=None, category=None):
    # check if the user is authenticated
    if not authenticate(request):
        return HttpResponseForbidden('You must provide a valid API key to access this view')

    if start_date and end_date and category:
        with connection.cursor() as cursor:
            query = """
                SELECT COUNT(*)
                FROM booking_room
                INNER JOIN booking_booking
                ON booking_room.room_id = booking_booking.room_id_id
                WHERE available = true
                AND category = %s
                AND start_date <= %s
                AND end_date >= %s
            """
            cursor.execute(query, [category, end_date, start_date])
            rooms = cursor.fetchone()[0]
            print(rooms)
    else:
        rooms = 0
    return render(request, 'room_count_by_category_range.html', context = {
        'rooms': rooms,
        'Room': Room,
    })

@require_POST
def room_count_by_category_range_submit(request):
    # check if the user is authenticated
    if not authenticate(request):
        return HttpResponseForbidden('You must provide a valid API key to access this view')

    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    category = request.POST.get('category')
    return redirect('room_count_by_category_range', start_date=start_date, end_date=end_date, category=category)

def guest_details(request, room_id=None):
    # check if the user is authenticated
    if not authenticate(request):
        return HttpResponseForbidden('You must provide a valid API key to access this view')

    if room_id:
        with connection.cursor() as cursor:
            query = """
                SELECT guest_name, phone_number
                FROM booking_booking
                WHERE room_id_id = %s
            """
            cursor.execute(query, [room_id])
            booking = dictfetchall(cursor)
            # print({'booking': booking})
    else:
        booking = None
    return render(request, 'guest_details.html', {'booking': booking})

@require_POST
def guest_details_submit(request):
    # check if the user is authenticated
    if not authenticate(request):
        return HttpResponseForbidden('You must provide a valid API key to access this view')

    room_id = request.POST.get('room_id')
    return redirect('guest_details', room_id=room_id)






#############################################  BY DJANGO ORM METHOD  ########################################################
""" def room_count_by_category(request, date=None):
    if date:
        rooms = Room.objects.filter(available=True).filter(booking__start_date__lte=date, booking__end_date__gte=date).values('category').annotate(count=Count('category'))
    else:
        rooms = []
    return render(request, 'room_count_by_category.html', {'rooms': rooms})

@require_POST
def room_count_by_category_submit(request):
    date = request.POST.get('date')
    return redirect('room_count_by_category', date=date)

def room_count_by_category_range(request, start_date=None, end_date=None, category=None):
    if start_date and end_date and category:
        rooms = Room.objects.filter(available=True, category=category).filter(booking__start_date__lte=end_date, booking__end_date__gte=start_date).count()
    else:
        rooms = 0
    return render(request, 'room_count_by_category_range.html', context = {
        'rooms': rooms,
        'Room': Room,
    })

@require_POST
def room_count_by_category_range_submit(request):
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    category = request.POST.get('category')
    return redirect('room_count_by_category_range', start_date=start_date, end_date=end_date, category=category)


def guest_details(request, room_id=None):
    if room_id:
        booking = Booking.objects.filter(room_id=room_id).values('guest_name', 'phone_number')
    else:
        booking = None
    return render(request, 'guest_details.html', {'booking': booking})

@require_POST
def guest_details_submit(request):
    room_id = request.POST.get('room_id')
    return redirect('guest_details', room_id=room_id) """





