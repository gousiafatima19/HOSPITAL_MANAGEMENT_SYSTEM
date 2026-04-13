from django.urls import path
from .views import appointment_list, appointment_create , appointment_edit , appointment_delete

urlpatterns = [
    path('', appointment_list, name='appointments'),
    path('create/', appointment_create, name='create_appointment'),
    path('<int:id>/edit/', appointment_edit, name='edit_appointment'),
    path('<int:id>/delete/', appointment_delete, name='delete_appointment'),
]