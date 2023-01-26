from django.db import models

from accounts.models import User


class Word(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='words')
    word = models.CharField(max_length=128)
    translation = models.CharField(max_length=128)
    description = models.TextField(default='...', blank=True)
    repeated = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'word')

    def add_repeat(self):
        self.repeated += 1
        self.save()

    def __str__(self):
        return f'{self.word} - {self.repeated}'
