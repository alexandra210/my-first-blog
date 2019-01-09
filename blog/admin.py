from django.contrib import admin
from .models import Medicine
from .models import Request

admin.site.register(Medicine)
admin.site.register(Request)

# Register your models here.
