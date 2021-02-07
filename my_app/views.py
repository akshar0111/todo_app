from django.shortcuts import render, redirect
from .models import item_model
from .forms import item_form
# Create your views here.

def home(request):
    #form = item_form()
    items = item_model.objects.all().order_by('-id')
    items_left = item_model.objects.filter(active='False').count()
    if request.method == 'POST':
        title = request.POST.get('item_title', '')
        if request.POST.get('checkbox', '') == 'on':
            active = True
        else:
            active = False
        obj = item_model(title=title, active=active)
        obj.save()
        return redirect('/')
    return render(request, 'home.html', {'items':items, 'item_left':items_left})

def active(request):
    items = item_model.objects.filter(active='False').order_by('-id')
    items_left = item_model.objects.filter(active='False').count()
    return render(request, 'home.html',{'items':items, 'item_left':items_left})

def completed(request):
    items = item_model.objects.filter(active='True').order_by('-id')
    items_left = item_model.objects.filter(active='False').count()
    return render(request, 'home.html',{'items':items, 'item_left':items_left})

def update_active(request, pk):
    item = item_model.objects.get(id=pk)
    item.active = not item.active
    item.save()
    return redirect('/')
def delete(request, pk):
    item = item_model.objects.get(id=pk)
    item.delete()
    return redirect('/')