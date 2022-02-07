from django.contrib import admin
from django.urls import path
from .views import StatsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',StatsView.as_view(),name='stats'),
]