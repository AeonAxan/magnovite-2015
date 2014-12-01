from django.db import models

from multiselectfield import MultiSelectField


class Event(models.Model):
    TECHNICAL_TAGS = (
        ('cse', 'Computer Science'),
        ('ec', 'Electronics'),
        ('mech', 'Mechanical'),
        ('civil', 'Civil'),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(help_text='The event url, use all simple and - as a seperator, Eg: junkyard-wars')

    quote = models.CharField(max_length=50, help_text='Text displayed on the cards in /events/')

    # This is assumed to be a Markdown field
    info = models.TextField(help_text='Please write in Markdown (Use headings, bold, italic, lists)')

    cash_prize = models.IntegerField(help_text='Numeric, Eg: 5000')

    # Time and venue are simple text
    date = models.IntegerField(max_length=2, help_text='Eg: 21')
    time = models.CharField(max_length=30, help_text='(Start time), Eg: 2pm')
    venue = models.CharField(max_length=50, help_text='Eg: Room 243, Block 2')

    # if not technical, then cultural
    technical = models.BooleanField(default=True, help_text='If cultural set to false')

    # This is a comma seperated field
    tags = MultiSelectField(choices=TECHNICAL_TAGS, blank=True, null=True)

    cover_picture = models.ImageField(
        upload_to='covers/',
        blank=True,
        null=True
    )

    def type(self):
        if self.technical:
            return 'technical'
        else:
            return 'cultural'

    def class_string(self):
        return ' '.join(map(lambda x: x.lower(), self.tags))

    def __str__(self):
        return self.title


class Registration(models.Model):
    event = models.ForeignKey(Event)
    profile = models.ForeignKey('main.Profile')

    # If this registration is for a team event
    # then the team id
    team_id = models.IntegerField(blank=True, null=True)
