from django.contrib import admin
from .models import (Author, Book, Narrator, Audiobook)
# class AuthorAdmin(admin.ModelAdmin):
# 	fields = ['name']
# class BookAdmin(admin.ModelAdmin):
# 	fields = ['title', 'description']


# Register your models here.

admin.site.register([Author, Book, Narrator, Audiobook])
