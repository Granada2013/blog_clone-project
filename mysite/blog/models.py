from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True)  # since it's a single-user blog (the authorized user is an author)
    title = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """
        Sets the published_date and saves the post in the database.
        """
        self.pudlished_date = timezone.now()
        self.save()

    def approve_comment(self):
        """
        Returns the list of approved comments to the current post.
        """
        return self.comments.filter(approved=True)

    def get_absolute_url(self):
        """
        Built-in django method indicates where to redirect a user after he creates a post.
        """
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved = models.BooleanField(default=False)

    def approve(self):
        """
        Sets the "approved" attribute of the comment to "True" and saves the comment in the datadase.
        """
        self.approved = True
        self.save()

    def get_absolute_url(self):
        """
        Built-in django method indicates where to redirect a user after he creates a post.
        """
        return reverse('blog:post_list')

    def __str__(self):
        return self.text

