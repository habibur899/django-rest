from django.contrib import admin

# Register your models here.
from .models import Aiquest


@admin.register(Aiquest)
class AiquestAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'course_name', 'course_duration', 'seat')
