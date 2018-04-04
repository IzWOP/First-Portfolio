from django.db import models

class Post(models.Model):
    title = models.CharField(blank=True, max_length=45)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
