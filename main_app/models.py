from django.db import models
from django.urls import reverse

# Create your models here.
class Subscription(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  image = models.CharField(max_length=100, default="")

  def save(self, *args, **kwargs):
    if not self.image:
      self.image = '/images/' + self.name.replace(" ", "").lower() + '.png'
    return super().save(*args, **kwargs)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("subs_detail", kwargs={"sub_id": self.id})

class Purchase(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=6, decimal_places=2)


  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("purchases_detail", kwargs={"purchase_id": self.id})
  