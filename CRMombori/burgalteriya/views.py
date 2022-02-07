from django.shortcuts import render,redirect
from django.views import View
from .models import Burgalter
from app1.models import Ombor,Product,Client
from statistika.models import Stats

class BurgalterView(View):
    def get(self,request):
        bug=Burgalter.objects.all()
        o=Ombor.objects.get(user=request.user)
        c=Client.objects.filter(ombor=o)
        p=Product.objects.filter(ombor=o)
        s=Stats.objects.filter(ombor=o)
        return render(request,'burgalter.html',{"all_bugal":bug,"clients":c,'products':p,"stats":s})
    def post(self,request):
        t=request.POST['tolagan_puli']
        q=request.POST['qarz_minus']
        p=request.POST['product']
        c=request.POST['client']
        m=request.POST['tavar_miqdori']
        pe=request.POST['tavarga_tolagan_puli']
        n=request.POST['nasiyasi']
        s=request.POST['stats']
        Burgalter.objects.create(
            product=Product.objects.get(id=p),
            client=Client.objects.get(id=c),
            stats=Stats.objects.get(id=s),
            som_sana=request.POST['som_sana'],
            tolagan_puli=t,
            qarz_minus=q,
            tavar_miqdori=m,
            tavarga_tolagan_puli=pe,
            nasiyasi=n,
            ombor=Ombor.objects.get(user=request.user)

        )
        cl=Client.objects.get(id=c)
        cl.qarz=int(cl.qarz)-int(t)
        cl.save()
        stats=Stats.objects.get(id=s)
        stats.umumiy_summa=int(stats.umumiy_summa)-int(pe)
        stats.save()
        return redirect('bug')



