from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='home'),
    path('delete/<int:id>',views.delete,name="delete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



