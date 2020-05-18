from django.urls import path
from django.conf.urls.static import static
from django.conf import settings 

from .views import RoomsListView

urlpatterns = [
    path('rooms', RoomsListView.as_view(), name='roomslistview'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
