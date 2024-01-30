from collections.abc import Iterable
from django.db import models


class Feed(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField(max_length=3000)
    published_at = models.DateTimeField(auto_now_add=True)
    views_count = models.PositiveIntegerField(default=0, editable=False)

    # class Meta:
    #     ordering = ("-published_at",)

    def __str__(self) -> str:
        return f"{self.title[:15]}..."

    def get_representation_title(self):
        #['Keçmiş', 'şirkət', 'direktoru', 'Ramiz', 'Mehdiyevin', 'xanımını', 'yenidən', 'məhkəməyə', 'verdi']
        words = self.title.split()
        limit = 80
        text = ""
        for word in words:
            if len(text + word) < limit:
                text += f" {word}"
            else:
                break
        else:
            return f"{text}"
        return f"{text}..."