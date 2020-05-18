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