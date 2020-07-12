from django.db import models


class MyBlog(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'MyBlog'

    def __str__(self):
        return f"{self.title}"
