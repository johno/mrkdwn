from django.db import models

class Note(models.Model)
  title        = models.CharField(max_length=100)
  published_at = models.DateTimeField('date published')
  content      = models.TextField()
