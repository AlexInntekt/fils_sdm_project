from datetime import datetime

from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect

from .models import Room, Booking, Checkin


class AdminView(TemplateView):
    template_name = 'admin.html'



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
