from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True)  # since an authorized user is an author
    title = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def save_as_draft(self):
        """
        Sets published_date to None and saves post as draft
        """
        self.published_date = None
        self.save()

    def publish(self):
        """
        Sets the published_date and saves the post in the database.
        """
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        """
        Built-in django method indicates where to redirect a user after he creates a post.
        """
        return reverse('blog:home')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        """
        Built-in django method indicates where to redirect a user after he creates a post.
        """
        return reverse('blog:post_list')

    def __str__(self):
        return self.text

