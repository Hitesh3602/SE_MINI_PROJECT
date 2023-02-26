from django.urls import include, path
from . import views

urlpatterns = [
    path('form/',views.form,name='form'),
    path('insert/',views.insert,name='insert'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('fetch/',views.fetch,name='fetch'),
    path('logout/',views.logout,name='logout'),   
]