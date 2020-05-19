from django.urls import path
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib.auth.views import LoginView, LogoutView

from .views import AddBookingView, BookingEditView, BookingsListView, AdminView, RoomsListView, RoomDetailView, RoomAddView, AddCheckinView, CheckinsListView, CheckinEditView

urlpatterns = [
    path('', AdminView.as_view(), name='admin'),
    path('rooms', RoomsListView.as_view(), name='rooms'),
    path('room/id=<int:id>', RoomDetailView.as_view(), name='room'),
    path('rooms/add', RoomAddView.as_view(), name='addroom'),
    path('checkins', CheckinsListView.as_view(), name='checkins'),
    path('checkin/id=<int:id>', CheckinEditView.as_view(), name='editcheckin'),
    path('checkins/add', AddCheckinView.as_view(), name='addcheckin'),
    path('bookings', BookingsListView.as_view(), name='bookings'),
    path('booking/id=<int:id>', BookingEditView.as_view(), name='booking'),
    path('bookings/add', AddBookingView.as_view(), name='addbooking'),
    path('login/$', LoginView.as_view(), name='login'),
    path('logout/$', LogoutView.as_view(), name='logout'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
