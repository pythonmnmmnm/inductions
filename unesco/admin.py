#/home/mnmmnm/django_projects/mysite/unesco/admin.py
from django.contrib import admin

# Register your models here.

from unesco.models import Site, Category, Iso,Region,States

admin.site.register(Site)
admin.site.register(Category)

admin.site.register(Iso)
admin.site.register(Region)

admin.site.register(States)