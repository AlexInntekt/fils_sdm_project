from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Room, Booking, Checkin


class AdminView(TemplateView):
    template_name = 'admin.html'


class RoomsListView(TemplateView):
    template_name = 'roomslist.html'


    def get(self, request, *args, **kwargs):

        context = {}

        context['rooms'] = Room.objects.all()

        return render(request, self.template_name, context)


class RoomDetailView(TemplateView):
    template_name = 'room.html'

    def get(self, request, *args, **kwargs):

        room_id = kwargs['id']
        room = Room.objects.get(id=room_id)
        context = {}

        context['room'] = room
        return render(request, self.template_name, context)
