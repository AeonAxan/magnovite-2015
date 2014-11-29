from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    quote = models.CharField(max_length=50)
    info = models.TextField()
    cash_prize = models.IntegerField()
    time = models.CharField(max_length=30)
    venue = models.CharField(max_length=50)

    # cover_picture = models.ImageField(upload_to='covers/')

    def __str__(self):
        return self.title
