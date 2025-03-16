from django.db import models

''''
Author model represents an author with a name
Book model represent a book with a title, publication year and a reference to its author.

'''

class Author(models.Model):
    name = models.CharField(max_length=100)
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
