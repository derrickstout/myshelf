from django.contrib import admin
from .models import (Author, Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	fieldsets = [
		('Details', {'fields': ['title','description','book_type', 'authors', 'series']}),
		('User Input', {'fields': ['review', 'finished',]}),
	]
	list_display = ("title", "list_authors", "series", "book_type", "finished",)

	list_editable = ("finished", "book_type",)

	list_filter = ("finished", "authors")


# Removing this model for now as it seems redundant for what I want to do
# @admin.register(Audiobook)
# class AudiobookAdmin(admin.ModelAdmin):
# 	fieldsets = [
# 		('Details', {'fields': ['title','description', 'authors', 'narrator', 'series']}),
# 		('User Input', {'fields': ['review', 'finished']}),
# 	]

# Register your models here.

admin.site.register([Author])
