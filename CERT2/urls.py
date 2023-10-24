from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('', views.comunicados, name="home"),
    path('admin/', admin.site.urls),
]
