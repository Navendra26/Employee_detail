
from django.contrib import admin
from django.urls import path
from my_app import views

#import below two things for including file in any of the models (i.e. settings and static)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='home'),  # send to views index function
    path("about", views.about, name='about'),  # send to views about function
    path("services", views.services, name='services'),  # send to views services function
    path("contact", views.contact, name='contact'),  # send to views contact function
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
    path("add_emp", views.addEmp, name='add_emp'),
    path("all_emp", views.allEmp, name='all_emp'),
    path("remove_emp", views.removeEmp, name='remove_emp'),
    path("remove_emp/<int:emp_id>", views.removeEmp, name='remove_emp'),
    path("filter_emp", views.filterEmp, name='filter_emp'),
]

#give permission to folder that file can get in this urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    