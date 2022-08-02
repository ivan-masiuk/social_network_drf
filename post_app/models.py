from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author_fk = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    text = models.TextField(verbose_name="Post text")

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)


class Like(models.Model):
    author_fk = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post_fk = models.ForeignKey("post_app.Post", on_delete=models.CASCADE, related_name="likes")

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
