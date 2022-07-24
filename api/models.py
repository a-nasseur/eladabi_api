from pyexpat import model
from statistics import mode
from unicodedata import category
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    message = models.TextField()
    owner = models.ForeignKey(
        'auth.User', related_name='owner', on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.message


class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(null=True)
    excerpt = models.CharField(max_length=250)
    featured = models.BooleanField(null=True, default=False)
    author = models.ForeignKey(
        'auth.User', related_name='author', on_delete=models.CASCADE)
    category = models.ForeignKey(
        'Category', related_name='category', on_delete=models.CASCADE, null=True, blank=True)
    thumbnail = CloudinaryField('uploads')
    image = CloudinaryField('uploads')
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        # Slug automation
        original_slug = slugify(self.title)
        queryset = Article.objects.all().filter(slug__iexact=original_slug).count()

        count = 1

        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = Article.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        # Setting up featured article
        if self.featured:
            try:
                temp = Article.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except Article.DoesNotExist:
                print('entry does not exist')

        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
