from django.urls import path
from . import views


urlpatterns = [

    # Registration form
    path('', views.registration, name='registration'),

    # Show all registration data
    path('data/', views.registration_list, name='registration_list'),

    # Update
    path(
        'update/<int:id>/',
        views.registration_update,
        name='registration_update'
    ),

    # Delete
    path(
        'delete/<int:id>/',
        views.registration_delete,
        name='registration_delete'
    ),

]