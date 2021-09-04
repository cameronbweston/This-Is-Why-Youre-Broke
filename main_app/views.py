from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Purchase, Subscription
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
  total_price = 0;
  for sub in subs:
    total_price += sub.price

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
  return render(request, 'purchases/index.html', {'purchases': purchases})

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
  fields = '__all__'

class PurchaseDelete(LoginRequiredMixin, DeleteView):
  model = Purchase  
  success_url = '/purchases/'
