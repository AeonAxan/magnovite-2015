from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    quote = models.CharField(max_length=50)

    # This is assumed to be a Markdown field
    info = models.TextField(help_text='Please write in Markdown')

    cash_prize = models.IntegerField()

    # Time and venue are simple text
    time = models.CharField(max_length=30)
    venue = models.CharField(max_length=50)

    # if not technical, then cultural
    technical = models.BooleanField(default=True)

    # This is a comma seperated field
    tags = models.CharField(
        help_text='Comma seperated list of tags',
        max_length=100,
        blank=True,
        null=True
    )

    cover_picture = models.ImageField(
        upload_to='covers/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class Registration(models.Model):
    event = models.ForeignKey(Event)
    profile = models.ForeignKey('main.Profile')

    # If this registration is for a team event
    # then the team id
    team_id = models.IntegerField(blank=True, null=True)
