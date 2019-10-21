from django.template.defaulttags import url
import mainapp.views as mainapp
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.main),
    path('register/', mainapp.register),
    path('login/', mainapp.login),
    path('generation/', mainapp.generation),
]



