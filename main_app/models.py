from django.db import models
from django.urls import reverse

# Create your models here.
class Subscription(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=4, decimal_places=2)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("subs_detail", kwargs={"sub_id": self.id})
  