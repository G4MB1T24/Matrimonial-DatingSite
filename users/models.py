from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    Country = models.CharField(default="India", max_length=30)
    State = models.CharField(default="India", max_length=30)
    age = models.IntegerField(default=18)
    usersocialTWT = models.CharField(max_length=15, default="")
    usersocialINSTA = models.CharField(max_length=15, default="")
    usersocialFB = models.CharField(max_length=15, default="")
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

    def __str__(self):
        return f"{self.user.username} Profile"

    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (400, 500)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
