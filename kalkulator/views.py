from django.shortcuts import render
from . import models
# Create your views here.

def kalkulator(request):
    result = None
    operator = ""
    if request.method == "POST":
        operator = request.POST.get("operator", "")
        try:
            result = eval(operator, {"__builtins__":None}, {})
        except:
            result = "Error"
        models.History.objects.create(operator=operator, result=result)
    histories = models.History.objects.all().order_by('-date')[:18]
    if histories.count() > 18:
        histories[18:].delete()
    context = {
        'title':'Kalkulator',
        'heading': 'kalkulator beta',
        'result': result,
        'histories': histories,
    }
        
    return render(request,'kalkulator/index.html', context)

def suhu(request):
    result = None
    if request.method == "POST":
        number = float(request.POST.get("number",0))
        suhu_asal = request.POST.get("suhu_asal","")
        suhu_tujuan = request.POST.get("suhu_tujuan","")
        result = konversi_suhu(number,suhu_asal,suhu_tujuan)
        models.History_suhu.objects.create(number=number,suhu_asal=suhu_asal,suhu_tujuan=suhu_tujuan,result=result)
    histories = models.History_suhu.objects.all().order_by('-date')[:18]
    if histories.count() > 18:
        histories[18].delete()
    context = {
        'title':'Konversi Suhu',
        'heading': 'Konversi Suhu',
        'result': result,
        'histories':histories
    }
    return render(request,"kalkulator/suhu.html", context)

def konversi_suhu(number,asal,tujuan):
    if asal == "C":
        if tujuan == "F":
            return (number * 9/5) + 32
        elif tujuan == "K":
            return number + 273.15
        elif tujuan == "Re":
            return number * 4/5
        else:
            return number
    elif asal == "F":
        if tujuan == "C":
            return (number - 32) * 5/9
        elif tujuan == "K":
            return (number - 32) * 5/9 + 273.15
        elif tujuan == "Re":
            return (number -32) * 4/9
        else:
            return number
    elif asal == "K":
        if tujuan == "C":
            return number - 273.15
        elif tujuan == "F":
            return (number - 273.15) * 9/5 + 32
        elif tujuan == "Re":
            return (number - 273.15) * 4/5
        else:
            return number
    elif asal == "Re":
        if tujuan == "C":
                return number * 5/4
        elif tujuan == "F":
                return (number * 9/4) + 32
        elif tujuan == "K":
            return (number * 5/4) + 273.15
        else:
            return number

def panjang(request):
    result = None
    if request.method == "POST":
        number = float(request.POST.get("number", 0))
        satuan_asal = request.POST.get("satuan_asal","")
        satuan_tujuan = request.POST.get("satuan_tujuan","")
        result = konversi_panjang(number,satuan_asal,satuan_tujuan)
        models.History_panjang.objects.create(number=number,panjang_asal=satuan_asal , result=result, panjang_tujuan=satuan_tujuan)
    histories = models.History_panjang.objects.all().order_by('-date')[:18]
    if histories.count() > 18:
        histories[18:].delete()
    context = {
        'title': 'Konversi Panjang',
        'heading':'Konversi Satuan Panjang',
        'result': result,
        'histories': histories
    }
    return render(request, 'kalkulator/panjang.html', context)

def konversi_panjang(number, asal, tujuan):
    satuan = {
        'km': 1000,
        'hm': 100,
        'dam' : 10,
        'm': 1,
        'dm': 0.1,
        'cm': 0.01,
        'mm': 0.001,
    }
    if asal in satuan and tujuan in satuan:
        return number * (satuan[asal] / satuan[tujuan])
    return None