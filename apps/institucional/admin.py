from django.contrib import admin

from .models import Autoridades, Cargo

# Register your models here.
admin.site.register(Cargo)
admin.site.register(Autoridades)