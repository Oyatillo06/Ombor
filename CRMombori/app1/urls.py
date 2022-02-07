from django.contrib import admin
from django.urls import path
from .views import BolimView,HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',BolimView.as_view(),name='bolim'),


]
