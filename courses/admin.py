from django.contrib import admin
from .models import Subject, Module, Course, Content

@admin.register(Subject)
class Subject(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title', )}

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ['title', 'subject', 'slug']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug' : ('title', )}
    inlines = [ModuleInline]

admin.site.register(Content)