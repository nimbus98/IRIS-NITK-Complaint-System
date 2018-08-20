from django.conf.urls import url
from django.urls import path

from . import views


app_name = 'Portalapp'
urlpatterns = [

    path('', views.index, name='index'),
	path('complaint/', views.complaint, name='complaint'),
	path('confirmation/', views.confirmation, name='confirmation'),
    path('Admin/', views.Admin, name='Admin'),
	path('adminsite_approval/', views.approval, name='approval'),
	path('adminsite/', views.adminsite, name='adminsite'),
	path('usersite/', views.usersite, name='usersite'),
]