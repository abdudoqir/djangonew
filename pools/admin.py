from django.contrib import admin

# Register your models here.
from .models import *


class QuestionsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Questions, QuestionsAdmin)
