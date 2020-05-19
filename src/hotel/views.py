from datetime import datetime
from collections import namedtuple

from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.db.models import Q

from .models import Room, Booking, Checkin


class AdminView(TemplateView):
    template_name = 'admin.html'

class CheckinEditView(TemplateView):
    template_name = 'edit_checkin.html'

    def get(self, request, *args, **kwargs):

        checkin_id = kwargs['id']
        checkin = Checkin.objects.get(id=checkin_id)
        context = {}

        context['checkin'] = checkin
        return render(request, self.template_name, context)



    def post(self, request, *args, **kwargs):
        context = {}
        post = request.POST
        print(post)

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
                    context['error'] = "Some old checkins overlap! Checkin with ID"+str(current_checkins.first().id)
        except Exception as e:
            context['error'] = "One problem occured: "+str(e)
        return render(request, self.template_name, context)

    def do_dates_overlap(cdate1,cdate2,ddate1,ddate2):
        Range = namedtuple('Range', ['start', 'end'])
        r1 = Range(start=datetime(cdate1), end=datetime(cdate2))
        r2 = Range(start=datetime(ddate1), end=datetime(ddate2))
        latest_start = max(r1.start, r2.start)
        earliest_end = min(r1.end, r2.end)
        delta = (earliest_end - latest_start).days + 1
        overlap = max(0, delta)

        if(overlap>0):
            return True
        else:
            return False

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
