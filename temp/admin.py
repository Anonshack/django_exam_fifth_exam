from django.contrib import admin
from .models import Person
# Register your models here.
search_fields = ['full_name']

admin.site.register(Person)