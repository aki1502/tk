from django.conf import settings
from django.db import models
from django.utils import timezone


class Akeet(models.Model):
    if False:
        childs = None
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey("akitter.Akeet", on_delete=models.CASCADE, related_name="childs", null=True)
    text = models.CharField(max_length=31)
    published_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.text)[:10]
