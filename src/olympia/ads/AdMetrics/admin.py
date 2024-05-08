from django.contrib import admin

# Register your models here.
from .models import Ads

from .models import AdTracking

admin.site.register(Ads)

admin.site.register(AdTracking)