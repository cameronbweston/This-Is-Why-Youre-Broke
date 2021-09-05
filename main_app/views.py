from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Purchase, Subscription, Photo
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'this-is-why-youre-broke'

# Create your views here.
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('subs_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  
class Home(LoginView):
  template_name = 'home.html'

def premiumcontent(request):
  return render(request, 'premiumcontent.html')

#Subscription Views
@login_required
def subs_index(request):
  subs = Subscription.objects.filter(user = request.user)
  price = subs.aggregate(Sum('price'))
  total_price = price['price__sum']

  return render(request, 'subscriptions/index.html', {'subs' : subs, 'total_price': total_price})

@login_required
def subs_detail(request, sub_id):
  sub = Subscription.objects.get(id = sub_id)
  return render(request, 'subscriptions/detail.html', {'sub': sub})

class SubCreate(LoginRequiredMixin, CreateView):
  model = Subscription
  fields = ['name', 'price']
  success_url = '/subscriptions/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class SubUpdate(LoginRequiredMixin, UpdateView):
  model = Subscription
  fields = '__all__'

class SubDelete(LoginRequiredMixin, DeleteView):
  model = Subscription
  success_url = '/subscriptions/'

#Purchase Views
@login_required
def purchases_index(request):
  purchases = Purchase.objects.filter(user = request.user)
  price = purchases.aggregate(Sum('price'))
  total_price = price['price__sum']

  return render(request, 'purchases/index.html', {'purchases': purchases, 'total_price': total_price})

@login_required
def purchase_detail(request, purchase_id):
  purchase = Purchase.objects.get(id = purchase_id)
  return render(request, 'purchases/detail.html', {'purchase': purchase})

class PurchaseCreate(LoginRequiredMixin, CreateView):
  model = Purchase
  fields = ['name', 'price']
  success_url = '/purchases/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PurchaseUpdate(LoginRequiredMixin, UpdateView):
  model = Purchase
  fields = ['name', 'price']

class PurchaseDelete(LoginRequiredMixin, DeleteView):
  model = Purchase  
  success_url = '/purchases/'

def add_photo(request, purchase_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to cat_id or cat (if you have a cat object)
      photo = Photo(url=url, purchase_id = purchase_id)
      # Remove old photo if it exists
      purchase_photo = Photo.objects.filter(purchase_id = purchase_id)
      if purchase_photo.first():
        purchase_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('purchase_detail', purchase_id = purchase_id)