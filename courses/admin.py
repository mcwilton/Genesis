from django.contrib import admin

from .models import Category, Course, Lesson


class CourseAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Category, CategoryAdmin)
# admin.site.register(Course, CourseAdmin)
# admin.site.register(Lesson)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'level', 'created_at', 'is_published')
    list_filter = ('category', 'price', 'is_published')
    search_fields = ('category', 'price', 'is_published')

@admin.register(Lesson)
class Lesson(admin.ModelAdmin):
    list_display = ('course', 'title', 'duration', 'created_at')
    list_filter = ('course', 'title')
    search_fields = ('course', 'title')

# @admin.register(Accredited_Program)
# class Accredited_ProgramAdmin(admin.ModelAdmin):
#     list_display = ('title', 'certificate_type', 'mode_of_delivery', 'nfq_level', 'duration', 'is_published')
#     list_filter = ('status', 'nfq_level', 'duration')
#     search_fields = ('title', 'nfq_level', 'duration')