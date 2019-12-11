from django.db import models
from .author import Author

class Books (models.Model):
    bookname = models.CharField(max_length=200,
                                default=None, null=True)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE,
                                    related_name='book_author')