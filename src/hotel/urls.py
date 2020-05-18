from django.urls import path

from .views import RoomsListView

urlpatterns = [
    path('rooms', RoomsListView.as_view(), name='roomslistview'),
]