from django.urls import path
from django.conf.urls.static import static
from django.conf import settings 

from .views import AdminView, RoomsListView, RoomDetailView, RoomAddView

urlpatterns = [
    path('', AdminView.as_view(), name='admin'),
    path('rooms', RoomsListView.as_view(), name='rooms'),
    path('room/id=<int:id>', RoomDetailView.as_view(), name='room'),
    path('rooms/add', RoomAddView.as_view(), name='addroom')

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
