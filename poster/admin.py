from django.contrib import admin
from .models import Category, Post, Customer
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['name']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['name', 'post']
    summernote_fields = ('message')


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'address', 'status', 'created_on')
    search_fields = ['title', 'description', 'color', 'cost']
    list_filter = ('status', 'approved', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)
    actions = ['approve_post']

    def approve_post(self, request, queryset):
        queryset.update(approved=True)


