"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from employee import views
from django.urls import include
from django.views.generic.base import TemplateView
from django.conf import settings 
from django.conf.urls.static import static 
from employee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #Company paths 
    path('dept', views.dept),
    path('show', views.show),
    path('edit/<str:cName>', views.edit),
    path('update/<str:cName>', views.update),
    path('delete/<str:cName>', views.delete), 

    #employee paths
    path('emp', views.emp),
    path('showemp', views.showemp),
    path('deleteEmp/<str:eFname>', views.deleteEmp),
    path('editemp/<str:eFname>', views.editemp), 
    path('updateEmp/<str:eFname>', views.updateEmp),
    path('searchem/',views.searchem,name='searchem'),
    path('searchde/',views.searchde,name='searchde'),
    path('sortaem',views.sortaem,name='sortaem'),
    path('sortdem',views.sortdem,name='sortdem'),
     path('sortade',views.sortade,name='sortade'),
    path('sortdde',views.sortdde,name='sortdde'),
    #Homepage path
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    #inbuilt login path
    path('accounts/', include('django.contrib.auth.urls')),
]