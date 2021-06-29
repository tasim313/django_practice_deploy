from django.contrib import admin
from .models import Customer
from .music_models import musicians, album

# Register your models here.

admin.site.register(Customer)
admin.site.register(musicians)
admin.site.register(album)