from django.contrib import admin
from .models import (Author, Book, Narrator, Audiobook)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	fieldsets = [
		('Details', {'fields': ['title','description', 'authors', 'series']}),
		('User Input', {'fields': ['review', 'finished']}),
	]
	list_display = ("title", "series", "finished")

	list_editable = ("finished",)

@admin.register(Audiobook)
class AudiobookAdmin(admin.ModelAdmin):
	fieldsets = [
		('Details', {'fields': ['title','description', 'authors', 'narrator', 'series']}),
		('User Input', {'fields': ['review', 'finished']}),
	]

# Register your models here.

admin.site.register([Author, Narrator])
