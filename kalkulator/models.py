from django.db import models
from django.utils import timezone
# Create your models here.
class History(models.Model):
    operator = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.operator} = {self.result} (on {self.date})"
    
class History_suhu(models.Model):
    number = models.FloatField()
    suhu_asal = models.CharField(max_length=255)
    result = models.FloatField()
    suhu_tujuan = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.number} {self.suhu_asal} = {self.result} {self.suhu_tujuan} (on {self.date})"
    
class History_panjang(models.Model):
    number = models.FloatField()
    panjang_asal = models.CharField(max_length=255)
    result = models.FloatField()
    panjang_tujuan= models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return f"{self.number} {self.panjang_asal} = {self.result} {self.panjang_tujuan} (on {self.date})"