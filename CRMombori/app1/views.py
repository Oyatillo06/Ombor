from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import *


class HomeView(View):
    def get(self,request):
        return render(request,'index.html')
    def post(self,request):
        u= request.POST.get('login')
        p=request.POST['password']
        users=authenticate(request,username=u,password=p)
        if users is None:
            return redirect('login')
        else:
            login(request,users)
            return redirect('bolim')

class BolimView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request, 'bulimlar.html')
        else:
            return redirect('login')



class Client_updateView(View):
    def get(self,request,son):
        if request.user.is_authenticated:
            client=Client.objects.get(id=son)

            return render(request, 'client_update.html',{'client':client})
        else:
            return redirect('login')
    def post(self,request,son):
        if request.user.is_authenticated:
            client=Client.objects.get(id=son)
            client.ism=request.POST['ism']
            client.tel=request.POST['tel']
            client.dokon_nomi=request.POST['dokon_nomi']
            client.joylashuv=request.POST['joylashuv']
            client.qarz=request.POST['qarz']
            client.save()
            return redirect('client')
        else:
            redirect('login')

class ClientView(View):
    def get(self,request):
        if request.user.is_authenticated:
            o=Ombor.objects.get(user=request.user)
            c=Client.objects.filter(ombor=o)
            return render(request, 'clients.html',{"all_clients":c})
        else:
            return redirect('login')
    def post(self,request):
        a=Ombor.objects.get(user=request.user)
        Client.objects.create(
            ism=request.POST['ism'],
            tel=request.POST['tel'],
            dokon_nomi=request.POST['dokon_nomi'],
            joylashuv=request.POST['joylashuv'],
            qarz=request.POST['qarz'],
            ombor=a

        )
        return redirect('client')
class Product_updateView(View):
    def get(self,request,son):
        if request.user.is_authenticated:
            product=Product.objects.get(id=son)
            return render(request, 'product_update.html',{"product":product})
        else:
            return redirect('login')
    def post(self,request,son):
        if request.user.is_authenticated:
            product=Product.objects.get(id=son)
            product.nom=request.POST['nom']
            product.brend_nomi=request.POST['brend_nomi']
            product.kelgan_narxi=request.POST['kelgan_narxi']
            product.sotuvdagi_narxi=request.POST['sotuvdagi_narxi']
            product.miqdor=request.POST['miqdor']
            product.save()
            return redirect('product')
        else:
            redirect('login')


class ProductView(View):

    def post(self,request):
        a=Ombor.objects.get(user=request.user)
        Product.objects.create(
            nom=request.POST['nom'],
            brend_nomi=request.POST['brend_nomi'],
            kelgan_narx=request.POST['kelgan_narxi'],
            sotuvdagi_narx=request.POST['sotuvdagi_narxi'],
            miqdor=request.POST['miqdor'],
            ombor=a

    )
        return redirect('product')
    def get(self,request):
        if request.user.is_authenticated:
            o=Ombor.objects.get(user=request.user)
            p=Product.objects.filter(ombor=o)
            return render(request, 'products.html',{'all_products':p})

        else:
            return redirect('login')


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')
