
from django.db import models
from django.utils import timezone


class Title(models.Model):
    title = models.CharField(max_length = 50)
    created_date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey('auth.User')

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.ForeignKey(Title, on_delete = models.CASCADE, blank = False, null = False)
    subtitle = models.CharField(max_length = 100)
    created_date = models.DateTimeField(default = timezone.now)
    description1 = models.TextField(blank = True, null = True)
    examples = models.TextField(blank = True, null = True)
    description2 = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.subtitle

