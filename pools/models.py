from django.db import models

# Create your models here.

from django.utils import timezone


class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data_published')

    def __str__(self):
        return f'{self.question_text}'


