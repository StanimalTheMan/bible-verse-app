from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

# Create your models here.
class Verse(models.Model):
    book = models.CharField(max_length=50)
    chapter = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    verse = models.PositiveIntegerField(validators=[MinValueValidator(1)]) # for simplicity's sake, one verse for now
    version = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.book + str(self.chapter) + ":" + str(self.verse) + "(" + self.version + ")"

    def get_absolute_url(self):
        return reverse('verse_detail', args=[str(self.id)])

# can put into another app later
class Comment(models.Model):
    verse = models.ForeignKey(
        Verse, 
        on_delete=models.CASCADE, 
        related_name='comments',
    )
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment 

    def get_absolute_url(self):
        return reverse('verse_list')
    