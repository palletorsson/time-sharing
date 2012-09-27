from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Userprofile(models.Model): 
    """
    UserProfile (kopplad till auth.user), edit profile 
    """
    user = models.OneToOneField(User)
    nick = models.CharField(max_length=40)


    def __unicode__(self):
        return unicode(self.user)
    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, **kwargs):
        Userprofile.objects.get_or_create(user=instance)