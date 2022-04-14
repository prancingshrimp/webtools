from django.contrib import admin

# Register your models here.
from .models import Question

from statics.models import UserProfile

admin.site.register(Question)
admin.site.register(UserProfile)