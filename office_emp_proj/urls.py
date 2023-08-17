"""
URL configuration for office_emp_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#manul change of admin page
admin.site.site_header = "Navendra Admin"
admin.site.index_title = "Welcome to Navendra Portal"
admin.site.site_title = "welcome to Navendra tutorials"

# every requested url passes through this projects >> url.py of project >> url.py of apps >> function of views.py of app
urlpatterns = [
    path('admin/', admin.site.urls),  #send to the admin path
    path('', include('my_app.urls'))  #send to the blank path

]
