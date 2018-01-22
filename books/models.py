from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=80, blank=False, null=False, unique=True)

	def __str__(self):
		return self.name

class Book(models.Model):
	PRINT = 'PRINT'
	AUDIO = 'AUDIO'
	EBOOK = 'EBOOK'
	BOOK_TYPE_CHOICES = (
		(PRINT, 'Print Book'),
		(AUDIO, 'Audiobook'),
		(EBOOK, 'eBook'),
		)
	#There has to be a better way to do this than multiple choice
	# NEXT_THREE_RANK_CHOICES	= (
	# 	(1, '1'),
	# 	(2, '2'),
	# 	(3, '3'),
	# 	)
	# next_three_rank = models.CharField(max_length=1, choices=NEXT_THREE_RANK_CHOICES, default='null', blank=True, null=True)
	book_type = models.CharField(max_length=5, choices=BOOK_TYPE_CHOICES, default='AUDIO')
	title = models.CharField(max_length=150)
	description = models.TextField(blank=True, null=True)
	series = models.CharField(max_length=150, blank=True, null=True)
	authors = models.ManyToManyField(Author, blank=True)
	review = models.TextField(blank=True, null=True)
	finished = models.BooleanField(default=False, verbose_name="Finished")
	# own = models.BooleanField(default=False)
	# image = models.ImageField()

	def __str__(self):
		return self.title

	def list_authors(self):
		return ", ".join([author.name for author in self.authors.all()])


# Removing to simplify, but saving in case I decide it makes sense later on
# class Narrator(models.Model):
# 	narrator = models.CharField(max_length=80)

# 	def __str__(self):
# 		return self.narrator

# class Audiobook(Book):
# 	length = models.CharField(max_length=20)
# 	narrator = models.ForeignKey(Narrator, on_delete=models.SET_NULL, blank=False, null=True)

# 	def __str__(self):
# 		return self.title