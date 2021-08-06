
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
    
    path('dept', views.dept),
    path('show', views.show),
    path('edit/<str:cName>', views.edit),
    path('update/<str:cName>', views.update),
    path('delete/<str:cName>', views.delete), 

   
    path('emp', views.emp),
    path('showemp', views.showemp),
    path('deleteEmp/<str:eFname>', views.deleteEmp),
    path('editemp/<str:eFname>', views.editemp), 
    path('updateEmp/<str:eFname>', views.updateEmp),
    path('searchem/',views.searchem,name='searchem'),
    path('searchde/',views.searchde,name='searchde'),
    path('sorta',views.sorta,name='sorta'),
    
 
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

   
    path('accounts/', include('django.contrib.auth.urls')),

    
    path('sortdem',views.sortdem,name='sortdem'),
    path('sortade',views.sortade,name='sortade'),
    path('sortdde',views.sortdde,name='sortdde'),
    
] 