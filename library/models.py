from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.TextField(max_length=100, verbose_name="title")
    author = models.TextField(max_length=100, verbose_name="author")
    category = models.TextField(max_length=100, verbose_name="category")
    publish_date = models.DateField(verbose_name="publish_date",null=True)
    editorial = models.TextField(max_length=100, verbose_name="editorial")
    pages = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="pages")
    description = models.TextField(max_length=800, verbose_name="description")
    files = models.FileField(upload_to="pdfs",verbose_name="files")
    images = models.ImageField(upload_to="logos", null=True, blank=True,verbose_name="images")
    
    def __str__(self):
        return self.title
