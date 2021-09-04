from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Purchase, Subscription

# Create your views here.
def home(request):
  return render(request, 'home.html')

def premiumcontent(request):
  return render(request, 'premiumcontent.html')

#Subscription Views
def subs_index(request):
  subs = Subscription.objects.all()
  return render(request, 'subscriptions/index.html', {'subs' : subs})

def subs_detail(request, sub_id):
  sub = Subscription.objects.get(id = sub_id)
  return render(request, 'subscriptions/detail.html', {'sub': sub})

class SubCreate(CreateView):
  model = Subscription
  fields = ['name', 'price']
  success_url = '/subscriptions/'

class SubUpdate(UpdateView):
  model = Subscription
  fields = '__all__'

class SubDelete(DeleteView):
  model = Subscription
  success_url = '/subscriptions/'

#Purchase Views
def purchases_index(request):
  purchases = Purchase.objects.all()
  return render(request, 'purchases/index.html', {'purchases': purchases})

def purchase_detail(request, purchase_id):
  purchase = Purchase.objects.get(id = purchase_id)
  return render(request, 'purchases/detail.html', {'purchase': purchase})

class PurchaseCreate(CreateView):
  model = Purchase
  fields = '__all__'
  success_url = '/purchases/'

class PurchaseUpdate(UpdateView):
  model = Purchase
  fields = '__all__'

class PurchaseDelete(DeleteView):
  model = Purchase  
  success_url = '/purchases/'
