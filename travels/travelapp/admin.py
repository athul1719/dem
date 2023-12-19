from django.contrib import admin

from travelapp.models import destination
from travelapp.models import names
# Register your models here.
admin.site.register(destination)
admin.site.register(names)