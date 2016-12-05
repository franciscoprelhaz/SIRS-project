from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    #link UserProfile to user instance
    user = models.OneToOneField(User)
    #picture = models.ImageField(upload_to='profile_pictures', blank = True)

    def __unicode__(self):
        return self.user.usernme
