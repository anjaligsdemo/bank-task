from django.urls import path
from . import views
from .views import get_branches_by_district

urlpatterns = [
    path('home', views.home, name='home'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('userhome', views.userhome, name='userhome'),
    path('get-branches/', get_branches_by_district, name='get_branches'),
    path('logout', views.logout, name='logout'),
]
