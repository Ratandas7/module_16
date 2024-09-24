from django.db import models
from categorys . models import Category
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateField()

    def __str__(self):
        return self.title