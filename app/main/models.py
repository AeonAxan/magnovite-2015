from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
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
        user.save(using=self._db)
        return user


class MUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

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

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permission to view the app"
        return True

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
    year = models.IntegerField(blank=True, null=True, max_length=1, help_text='Studying in year (1, 2, 3, 4, 5)?')

    registered_events = models.ManyToManyField(Event, through=Registration)

    def is_complete(self):
        return self.name != '' and self.mobile != '' and \
            self.college != '' and \
            self.year != None and self.active_email != ''

    def __str__(self):
        return self.name
