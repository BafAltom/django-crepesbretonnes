from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.CharField(max_length=12)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Publication Date")
    categorie = models.ForeignKey('Categorie')

    def __unicode__(self):
        return u"%s" % self.title


class Categorie(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nom
