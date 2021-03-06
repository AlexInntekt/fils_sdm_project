from datetime import datetime
from collections import namedtuple

from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.db.models import Q

from .models import Room, Booking, Checkin


class AdminView(TemplateView):
    template_name = 'admin.html'


class AddBookingView(TemplateView):
    template_name = 'add_booking.html'

    def get(self, request, *args, **kwargs):

        context = {}
        context['rooms'] = Room.objects.all()
        return render(request, self.template_name, context)



    def post(self, request, *args, **kwargs):
        context = {}
        post = request.POST
        print(post)
        context['rooms'] = Room.objects.all()
        try:
            action = post['action']

            room = Room.objects.get(id=int(post['room']))
            customer = post['customer']
            starting_date = post['starting_date']
            end_date = post['end_date']

            booking = Booking()
            context['booking'] = booking

            booking.room = room
            booking.customer = customer
            booking.start_datetime = datetime.strptime(str(starting_date),'%Y-%m-%d')#starting_date
            booking.end_datetime = datetime.strptime(str(end_date),'%Y-%m-%d')
            booking.last_modified = datetime.now()

            Qd = Q() # & ~Q(id=booking.id)

            Qd |= Q(Q(Q(start_datetime__range=[starting_date, end_date]) | Q(end_datetime__range=[starting_date, end_date])) & Q(room__id=booking.room.id) & ~Q(id=booking.id))
            Qd |= Q(Q(Q(start_datetime__lte=starting_date) & Q(end_datetime__gte=end_date)) & Q(room__id=booking.room.id) & ~Q(id=booking.id))
            Qd |= Q(Q(Q(start_datetime__gte=starting_date) & Q(end_datetime__lte=end_date)) & Q(room__id=booking.room.id) & ~Q(id=booking.id))

            current_bookings = Booking.objects.filter(Qd)
            objs = current_bookings.count()
            print("\n\n")
            print(objs)
            if(objs==0):
                booking.save()
                context['booking'] = booking
                context['success'] = "The change was applied succesfully!"
            else:
                context['error'] = "Some old bookings overlap! Booking with ID "+str(current_bookings.first().id)
        except Exception as e:
            context['error'] = "One problem occured: "+str(e)
            print(e.__dict__)
        return render(request, self.template_name, context)


class BookingEditView(TemplateView):
    template_name = 'edit_booking.html'

    def get(self, request, *args, **kwargs):

        booking_id = kwargs['id']
        booking = Booking.objects.get(id=booking_id)
        context = {}

        context['booking'] = booking
        context['rooms'] = Room.objects.all()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        context['rooms'] = Room.objects.all()
        post = request.POST
        print(post)

        try:
            action = post['action']
            booking_id = kwargs['id']

            if action == 'delete':
                booking = Booking.objects.get(id=booking_id)
                bookingbooking.delete()
                return redirect('bookings')

            else:
                room = Room.objects.get(id=post['room'])
                customer = post['customer']
                starting_date = post['starting_date']
                end_date = post['end_date']

                booking = Booking.objects.get(id=booking_id)
                context['booking'] = booking

                booking.room = room
                booking.customer = customer
                booking.start_datetime = datetime.strptime(str(starting_date),'%Y-%m-%d')#starting_date
                booking.end_datetime = datetime.strptime(str(end_date),'%Y-%m-%d')
                booking.last_modified = datetime.now()

                Qd = Q() # & ~Q(id=checkin.id)

                Qd |= Q(Q(Q(start_datetime__range=[starting_date, end_date]) | Q(end_datetime__range=[starting_date, end_date])) & Q(room__id=booking.room.id) & ~Q(id=booking.id))
                Qd |= Q(Q(Q(start_datetime__lte=starting_date) & Q(end_datetime__gte=end_date)) & Q(room__id=booking.room.id) & ~Q(id=booking.id))
                Qd |= Q(Q(Q(start_datetime__gte=starting_date) & Q(end_datetime__lte=end_date)) & Q(room__id=booking.room.id) & ~Q(id=booking.id))

                current_bookings = Booking.objects.filter(Qd)
                objs = current_bookings.count()
                print("\n\n")
                print(objs)
                if(objs==0):
                    booking.save()
                    context['booking'] = booking
                    context['success'] = "The change was applied succesfully!"
                else:
                    context['error'] = "Some old checkins overlap! Booking with ID "+str(current_bookings.first().id)
        except Exception as e:
            context['error'] = "One problem occured: "+str(e)
        return render(request, self.template_name, context)


class AddCheckinView(TemplateView):
    template_name = 'add_checkin.html'

    def get(self, request, *args, **kwargs):

        context = {}
        context['rooms'] = Room.objects.all()
        return render(request, self.template_name, context)



    def post(self, request, *args, **kwargs):
        context = {}
        post = request.POST
        print(post)
        context['rooms'] = Room.objects.all()   
        try:
            action = post['action']

            room = Room.objects.get(id=int(post['room']))
            customer = post['customer']
            starting_date = post['starting_date']
            end_date = post['end_date']

            checkin = Checkin()
            context['checkin'] = checkin

            checkin.room = room
            checkin.customer = customer
            checkin.start_datetime = datetime.strptime(str(starting_date),'%Y-%m-%d')#starting_date
            checkin.end_datetime = datetime.strptime(str(end_date),'%Y-%m-%d')
            checkin.last_modified = datetime.now()

            Qd = Q() # & ~Q(id=checkin.id)

            Qd |= Q(Q(Q(start_datetime__range=[starting_date, end_date]) | Q(end_datetime__range=[starting_date, end_date])) & Q(room__id=checkin.room.id) & ~Q(id=checkin.id))
            Qd |= Q(Q(Q(start_datetime__lte=starting_date) & Q(end_datetime__gte=end_date)) & Q(room__id=checkin.room.id) & ~Q(id=checkin.id))
            Qd |= Q(Q(Q(start_datetime__gte=starting_date) & Q(end_datetime__lte=end_date)) & Q(room__id=checkin.room.id) & ~Q(id=checkin.id))

            current_checkins = Checkin.objects.filter(Qd)
            objs = current_checkins.count()
            print("\n\n")
            print(objs)
            if(objs==0):
                checkin.save()
                context['checkin'] = checkin
                context['success'] = "The change was applied succesfully!"
            else:
                context['error'] = "Some old checkins overlap! Checkin with ID "+str(current_checkins.first().id)
        except Exception as e:
            context['error'] = "One problem occured: "+str(e)
            print(e.__dict__)
        return render(request, self.template_name, context)




class CheckinEditView(TemplateView):
    template_name = 'edit_checkin.html'

    def get(self, request, *args, **kwargs):

        checkin_id = kwargs['id']
        checkin = Checkin.objects.get(id=checkin_id)
        context = {}
        context['rooms'] = Room.objects.all()
        context['checkin'] = checkin
        return render(request, self.template_name, context)



    def post(self, request, *args, **kwargs):
        context = {}
        post = request.POST
        print(post)
        context['rooms'] = Room.objects.all()
        try:
            action = post['action']
            checkin_id = kwargs['id']

            if action == 'delete':
                checkin = Checkin.objects.get(id=checkin_id)
                checkin.delete()
                return redirect('checkins')

            else:
                room = Room.objects.get(id=post['room'])
                customer = post['customer']
                starting_date = post['starting_date']
                end_date = post['end_date']

                checkin = Checkin.objects.get(id=checkin_id)
                context['checkin'] = checkin

                checkin.room = room
                checkin.customer = customer
                checkin.start_datetime = datetime.strptime(str(starting_date),'%Y-%m-%d')#starting_date
                checkin.end_datetime = datetime.strptime(str(end_date),'%Y-%m-%d')
                checkin.last_modified = datetime.now()

                Qd = Q() # & ~Q(id=checkin.id)

                Qd |= Q(Q(Q(start_datetime__range=[starting_date, end_date]) | Q(end_datetime__range=[starting_date, end_date])) & Q(room__id=checkin.room.id) & ~Q(id=checkin.id))
                Qd |= Q(Q(Q(start_datetime__lte=starting_date) & Q(end_datetime__gte=end_date)) & Q(room__id=checkin.room.id) & ~Q(id=checkin.id))
                Qd |= Q(Q(Q(start_datetime__gte=starting_date) & Q(end_datetime__lte=end_date)) & Q(room__id=checkin.room.id) & ~Q(id=checkin.id))

                current_checkins = Checkin.objects.filter(Qd)
                objs = current_checkins.count()
                print("\n\n")
                print(objs)
                if(objs==0):
                    checkin.save()
                    context['checkin'] = checkin
                    context['success'] = "The change was applied succesfully!"
                else:
                    context['error'] = "Some old checkins overlap! Checkin with ID "+str(current_checkins.first().id)
        except Exception as e:
            context['error'] = "One problem occured: "+str(e)
        return render(request, self.template_name, context)


class BookingsListView(TemplateView):
    template_name = 'bookings_list.html'


    def get(self, request, *args, **kwargs):

        context = {}

        context['bookings'] = Booking.objects.all()

        return render(request, self.template_name, context)

class CheckinsListView(TemplateView):
    template_name = 'checkins_list.html'


    def get(self, request, *args, **kwargs):

        context = {}

        context['checkins'] = Checkin.objects.all()

        return render(request, self.template_name, context)


class RoomsListView(TemplateView):
    template_name = 'roomslist.html'


    def get(self, request, *args, **kwargs):

        context = {}

        context['rooms'] = Room.objects.all()

        return render(request, self.template_name, context)

class RoomAddView(TemplateView):
    template_name = 'add_room.html'

    def get(self, request, *args, **kwargs):

        context = {}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        post = request.POST
        print(post)

        try:
            bed_type = post['bed_type']
            facilities = post['facilities']
            price = post['price']

            room = Room()

            room.bed_type = bed_type
            room.facilities = facilities
            room.price = price
            room.last_modified = datetime.now()
            room.save()

            # context['room'] = room
            context['success'] = "The change was applied succesfully!"
        except Exception as e:
            context['error'] = "One problem occured: "+str(e)
        return render(request, self.template_name, context)



class RoomDetailView(TemplateView):
    template_name = 'room.html'

    def get(self, request, *args, **kwargs):

        room_id = kwargs['id']
        room = Room.objects.get(id=room_id)
        context = {}

        context['room'] = room
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        post = request.POST
        print(post)

        try:
            action = post['action']
            room_id = kwargs['id']

            if action == 'delete':
                room = Room.objects.get(id=room_id)
                room.delete()
                return redirect('rooms')

            else:
                bed_type = post['bed_type']
                facilities = post['facilities']
                price = post['price']

                room = Room.objects.get(id=room_id)

                room.bed_type = bed_type
                room.facilities = facilities
                room.price = price
                room.last_modified = datetime.now()
                room.save()

                context['room'] = room
                context['success'] = "The change was applied succesfully!"
        except Exception as e:
            context['error'] = "One problem occured: "+str(e)
        return render(request, self.template_name, context)
