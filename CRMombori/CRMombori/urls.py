
from django.contrib import admin
from django.urls import path,include
from app1.views import HomeView,Client_updateView,ClientView,Product_updateView,ProductView,LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('bolim/',include('app1.urls')),
    path('',HomeView.as_view(),name='login'),
    path('client_update/<int:son>/',Client_updateView.as_view(),name='client_update'),
    path('client/',ClientView.as_view(),name='client'),
    path('product_update/<int:son>/',Product_updateView.as_view(),name='product_update'),
    path('product/',ProductView.as_view(),name='product'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('stats/',include('statistika.urls')),
    path('bug/',include("burgalteriya.urls")),




]
