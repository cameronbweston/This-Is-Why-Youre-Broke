from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('premiumcontent/', views.premiumcontent, name='premiumcontent'),
  #Subscription Views
  path('subscriptions/', views.subs_index, name='subs_index'),
  path('subs/<int:sub_id>/', views.subs_detail, name='subs_detail'),
  path('subs/create/', views.SubCreate.as_view(), name='subs_create'),
  path('subs/<int:pk>/update/', views.SubUpdate.as_view(), name='subs_update'),
  path('subs/<int:pk>/delete/', views.SubDelete.as_view(), name='subs_delete'),
  #Purchases Views
  path('purchases/', views.purchases_index, name='purchases_index'),
  path('purchases/<int:purchase_id>/', views.purchase_detail, name='purchase_detail'),
  path('purchases/create/', views.PurchaseCreate.as_view(), name='purchase_create'),
  path('purchases/<int:pk>/update/', views.PurchaseUpdate.as_view(), name='purchase_update'),
  path('purchases/<int:pk>/delete/', views.PurchaseDelete.as_view(), name='purchase_delete'),
  #User Signup
  path('accounts/signup/', views.signup, name='signup'),
  #Photos
  path('purchases/<int:purchase_id>/add_photo/', views.add_photo, name='add_photo'),
  #Investment Views
  path('investment/', views.investment_index, name='investment_index'),
]