from django.urls import path
from .views import formset_view

urlpatterns = [
   
    path('', formset_view, name='form'),
    ]
    