from django.db import models

# Create your models here


class Homeslider(models.Model):
    name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to="slider/")
    text1 = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        help_text="maximum of 40 charaters permitted",
    )
    text2 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        help_text="maximum of 30 charaters permitted",
    )
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name