from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class RoomsListView(TemplateView):
    template_name = 'roomslist.html'
