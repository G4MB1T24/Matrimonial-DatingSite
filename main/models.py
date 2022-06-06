from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse

# Create your models here.


class WedPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    defaultrel = ("Any", "Any")
    religion_choices = {
        ("Any", "Any"),
        ("Hindu", "Hindu"),
        ("Christian", "Christian"),
        ("Muslim", "Muslim"),
        ("Sikh", "Sikh"),
        ("Jain", "Jain"),
        ("Buddhist", "Buddhist"),
    }
    religion = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        choices=religion_choices,
        default=defaultrel,
    )
    date_posted = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
