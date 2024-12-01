import string
import random

from django.core.validators import validate_comma_separated_integer_list
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Post.STATUS.PUBLISHED)


class Post(models.Model):
    class STATUS(models.IntegerChoices):
        PRIVATE = 0, 'Private'
        PUBLISHED = 1, 'Published'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=STATUS.choices, default=STATUS.PUBLISHED)

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('posts:post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        base_slug = slugify(self.title)
        slug = base_slug
        counter = 1
        while Post.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{self.generate_suffix(counter)}"
            counter += 1
        return slug

    def generate_suffix(self, length):
        all_symbols = string.ascii_uppercase + string.digits + string.ascii_lowercase
        result = ''.join(random.choice(all_symbols) for _ in range(length))
        return result

    def get_files(self):
        return PostFiles.objects.filter(post=self)

    def get_edit_url(self):
        return reverse('posts:edit_post', kwargs={'post_slug': self.slug})


class PostFiles(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to='upload_posts_files/%Y/%m/%d/')
