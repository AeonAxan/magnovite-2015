from django.db import models


class Analytics(models.Model):
    date = models.DateField(auto_now_add=True)
    data = models.TextField()

    @staticmethod
    def capture():
        pass
