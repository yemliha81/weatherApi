from django.db import models

# Create your models here.
class Records(models.Model):
    city_name = models.CharField(max_length=30)
    current_temperature = models.CharField(max_length=30)
    today_min_temperature = models.CharField(max_length=30)
    today_max_temperature = models.CharField(max_length=30)
    this_week_min_temperature = models.CharField(max_length=30)
    this_week_max_temperature = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)