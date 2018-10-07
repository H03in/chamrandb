from django.db import models

# Create your models here.

class Gene(models.Model):
    code = models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    detail = models.TextField(max_length=500, default='')
    sequence = models.URLField()
    source = models.CharField(max_length=400)


class Source(models.Model):
    gene = models.ForeignKey(Gene, related_name='related_sources', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    url = models.URLField()


class Keyword(models.Model):
    name = models.CharField(max_length=100)
    gene = models.ForeignKey(Gene, related_name='keywords', on_delete=models.CASCADE)



