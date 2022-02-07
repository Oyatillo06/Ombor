from django.db import models

from app1.models import Client,Product,Ombor
from statistika.models import Stats
class Burgalter(models.Model):
    client=models.ForeignKey(Client,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL, null=True)
    stats=models.ForeignKey(Stats,on_delete=models.SET_NULL,null=True)
    som_sana=models.DateTimeField()
    tolagan_puli = models.IntegerField(blank=True)
    qarz_minus=models.IntegerField(blank=True)
    tavar_miqdori=models.IntegerField()
    tavarga_tolagan_puli=models.IntegerField()
    nasiyasi=models.IntegerField()
    ombor=models.ForeignKey(Ombor,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f"{self.client},{self.som_sana},{self.product}"





