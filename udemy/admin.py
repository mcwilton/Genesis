from django.contrib import admin

from .models import Enroll

@admin.register(Enroll)
class EnrollAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'created_at')
    list_filter = ('course', 'created_at')
    search_fields = ('course', 'created_at')