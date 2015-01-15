from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

from app.event.models import Event, Registration


class MUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and pwd
        """
        if not email:
            raise ValueError('User must have an email')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuse with the given email and pwd
        """
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False, help_text='Has access to admin site')

    objects = MUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Magnovite User'

    def save(self, *args, **kwargs):
        super(MUser, self).save(*args, **kwargs)
        if self.has_profile():
            return

        # Create a blank profile if the user doesnt have a profile
        p = Profile()
        p.user = self
        p.auth_provider = 'internal'
        p.active_email = self.email
        p.save()

    def has_profile(self):
        try:
            self.profile
            return True
        except Profile.DoesNotExist:
            return False

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(MUser, null=True)

    # auth provider
    auth_provider = models.CharField(max_length=30, blank=True)

    # this will be initialized to user.email
    # This will be used for commmunication and we will
    # let the user change this. user.email will be the one
    # we got from social_provider
    active_email = models.EmailField()

    # basic details
    name = models.CharField(blank=True, max_length=50)
    mobile = models.CharField(blank=True, max_length=10, help_text='Without +91')
    college = models.CharField(blank=True, max_length=50)
    referral = models.CharField(
        blank=True, max_length=50,
        help_text='Referral: How did you find out about us?',
        default=''
    )

    registered_events = models.ManyToManyField(Event, through=Registration)

    # internal fields
    is_internal = models.BooleanField(
        default=False,
        help_text='Is this an internal account? (Event Heads, etc)'
    )
    events = models.ManyToManyField(Event,
        verbose_name='Events Incharge of',
        related_name='heads',
        help_text='The event this profile is in-charge of',
        null=True, blank=True
    )

    def first_name(self):
        if not self.name:
            return ''

        return self.name.split(' ')[0]

    def is_registered_to_event(self, event):
        return self.registered_events.filter(id=event.id).count() == 1

    def get_absolute_url(self):
        return '/profile/'

    def is_complete(self):
        return self.name != '' and self.mobile != '' and \
            self.college != '' and \
            self.active_email != ''

    def __str__(self):
        return str(self.id) + ', ' + self.name + '(' + self.active_email + ')'
