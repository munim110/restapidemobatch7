from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    profile_pic = models.ImageField(upload_to='images/', null=True, blank=True)
    bio = models.TextField()
    languages = models.ManyToManyField(Language)

    def __str__(self) -> str:
        return self.name
    


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    cover = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField()
    date_published = models.DateField()

    def __str__(self) -> str:
        return self.title
    

