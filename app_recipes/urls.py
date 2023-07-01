from django.contrib import admin
from django.urls import include, path
from app_recipes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home)
]