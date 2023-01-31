from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
        path('home/',views.Home.as_view(),name='home'),
        path('profile/',views.Profile.as_view(),name='profile'),
        path('staff/',views.Staffdetails.as_view(),name='staff'),
        path('students/',views.Addstudent.as_view(),name='students'),
        path('showstudents/',views.Showstudents.as_view(),name='showstudents'),
        path('enquiry/',views.Enquiry.as_view(),name='enquiry'),
        path('edit/',views.Edit.as_view(),name='edit'),
        path('delete/',views.Delete.as_view(),name='delete'),
        path('editprofile/',views.Editprofile.as_view(),name='editprofile'),




]