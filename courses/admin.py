from django.contrib import admin

from .models import Course, Text

class TextInline(admin.StackedInline):
    model = Text


class CourseAdmin(admin.ModelAdmin):
    inlines = [TextInline,]



admin.site.register(Course, CourseAdmin)
admin.site.register(Text)
