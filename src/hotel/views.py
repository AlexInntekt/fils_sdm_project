from datetime import datetime

from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect

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

                checkin.room = room
                checkin.customer = customer
                checkin.start_datetime = datetime.strptime(str(starting_date),'%Y-%m-%d')#starting_date
                checkin.end_datetime = datetime.strptime(str(end_date),'%Y-%m-%d')
                checkin.last_modified = datetime.now()

                Qd = Q((room__id=checkin.room.id) && ())
                current_checkins = Checkin.objects.filter(Qd)
                checkin.save()

                context['checkin'] = checkin
                context['success'] = "The change was applied succesfully!"
        except Exception as e:
            context['error'] = "One problem occured: "+str(e)
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
