from django.db import models


class Feed(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField(max_length=3000)
    published_at = models.DateTimeField(auto_now_add=True)
    views_count = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self) -> str:
        return f"{self.title[:10]}..."