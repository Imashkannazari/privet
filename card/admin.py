from . models import Programmers, Category, Projects
from django.contrib import admin

@admin.register(Programmers)
class ProgrammersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'email')
    search_fields = ('id', 'name', 'last_name', 'email')

    fieldsets = (
        (None, {
            'fields': ('id',)
        }),
        ('about', {
            'fields': ('name', 'last_name', 'email', 'phone', 'age',)
        }),
        ('descriptions', {
            'fields': ('description',)
        }),
        ('picture', {
            'fields': ('image',)
        }),
        ('Important dates', {
            'fields': ('joined',)
        }),
    )
    readonly_fields = ('joined','name', 'last_name', 'id')
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('id', 'title')
    fieldsets = (
        ('about', {
            'fields': ('title','description',)
        }),
        ('Important dates',{
            'fields': ('created',)
        }),
    )
    readonly_fields = ('created','title','description')

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'programmer_name', 'category')
    search_fields = ('id', 'title', 'description')
    list_filter = ('programmer_name', 'category',)
    fieldsets = (
        ('about', {
            'fields': ('title', 'description', 'category')
        }),
        ('programmers', {
            'fields': ('programmer_name', )
        }),
        ('Images', {
            'fields': ('image', )
        }),
        ('Important dates', {
            'fields': ('created',)
        })
    )
    readonly_fields = ('created',)