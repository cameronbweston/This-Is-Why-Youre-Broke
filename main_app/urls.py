from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('premiumcontent/', views.premiumcontent, name='premiumcontent'),
  path('subscriptions/', views.subs_index, name='subs_index'),
  path('subs/<int:sub_id>/', views.subs_detail, name='subs_detail'),
  path('subs/create/', views.SubCreate.as_view(), name='subs_create'),
  path('subs/<int:pk>/update/', views.SubUpdate.as_view(), name='subs_update'),
  path('subs/<int:pk>/delete/', views.SubDelete.as_view(), name='subs_delete'),
]