import os

from django.conf import settings
from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Akeet(models.Model):
    if False:
        childs = None
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="akeets")
    parent = models.ForeignKey("akitter.Akeet", on_delete=models.CASCADE, related_name="childs", null=True)
    text = models.CharField(max_length=31)
    published_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.text)[:10]
    

class Following(models.Model):
    followee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="followed", on_delete=models.CASCADE)
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="following", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.follower)+"->"+str(self.followee)


class UserInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="info", on_delete=models.CASCADE)
    origin = models.ImageField(upload_to="images/userimages/", default="images/userimages/default_image.png")
    image = ImageSpecField(
        source="origin",
        processors=[ResizeToFill(300, 300)],
        format="PNG",
        options={"quality": 60}
    )
    vio = models.CharField(max_length=31, blank=True)
