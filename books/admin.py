from django.contrib import admin
from .models import (Author, PrintBook, EBook, Narrator, Audiobook)

@admin.register(PrintBook, EBook)
class BookAdmin(admin.ModelAdmin):
	fieldsets = [
		('Details', {'fields': ['title','description', 'authors', 'series']}),
		('User Input', {'fields': ['review', 'finished',]}),
	]
	list_display = ("title", "list_authors", "series", "finished",)

	list_editable = ("finished",)

	list_filter = ("finished", "authors")


@admin.register(Audiobook)
class AudiobookAdmin(admin.ModelAdmin):
	fieldsets = [
		('Details', {'fields': ['title','description', 'authors', 'narrator', 'series']}),
		('User Input', {'fields': ['review', 'finished']}),
	]

	list_display = ("title", "list_authors", "series", "narrator", "finished")

	list_filter = ("narrator", "series", "finished")

# Register your models here.

admin.site.register([Author, Narrator])
