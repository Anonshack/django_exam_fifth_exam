from django.db import models
from django.urls import reverse


class Person(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='name')
    ish_joyi = models.CharField(max_length=255)
    age = models.IntegerField()
    birthday = models.DateField()
    info = models.TextField()

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

