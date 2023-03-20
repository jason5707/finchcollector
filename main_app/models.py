from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner'),
)
 
def __str__(self):
     return self.name


# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250) 
    
user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return f'{self.name} ({self.id})'  
    
def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id': self.id})

def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )

  cat = models.ForeignKey(
    Finch,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']


class Photo(models.Model):
  url = models.CharField(max_length=200)
  cat = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for cat_id: {self.cat_id} @{self.url}"