from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=80, blank=False, null=False, unique=True)

	def __str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField(blank=True, null=True)
	series = models.CharField(max_length=150, blank=True, null=True)
	authors = models.ManyToManyField(Author, blank=True)
	review = models.TextField(blank=True, null=True)
	finished = models.BooleanField(default=False, verbose_name="Finished")
	# image = models.ImageField()

	def __str__(self):
		return self.title

	def list_authors(self):
		return ", ".join([author.name for author in self.authors.all()])

class Narrator(models.Model):
	narrator = models.CharField(max_length=80)

	def __str__(self):
		return self.narrator

class Audiobook(Book):
	length = models.CharField(max_length=20)
	narrator = models.ForeignKey(Narrator, on_delete=models.SET_NULL, blank=False, null=True)

	def __str__(self):
		return self.title