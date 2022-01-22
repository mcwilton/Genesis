from django.contrib import admin

from .models import User

# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    list_filter = ('username', 'email')
    search_fields = ('username', 'email')
