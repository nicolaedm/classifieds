from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    category_title = models.CharField(max_length=200)

    def __str__(self):
        return self.category_title


class Add(models.Model):
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    add_text = models.CharField(max_length=200)

    def __str__(self):
        return self.add_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)