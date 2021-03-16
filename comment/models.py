from django.contrib.auth import get_user_model
from django.db import models

from term.models import Suggestion

User = get_user_model()


class Comment(models.Model):
    """Отзывы"""
    text = models.TextField("Комментарии", max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion = models.ForeignKey(Suggestion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text} - {self.author}"
