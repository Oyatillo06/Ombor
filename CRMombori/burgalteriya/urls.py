from django.contrib import admin
from django.urls import path
from .views import BurgalterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',BurgalterView.as_view(),name='bug'),
]