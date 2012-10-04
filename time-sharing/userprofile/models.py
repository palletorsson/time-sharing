from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from imagekit.models import ImageSpecField
#from imagekit.processors import ResizeToFill, Adjust


STATUS = ( (0, 'Active'), (1, 'NotActive'), )

class Userprofile(models.Model): 
    """
    UserProfile (kopplad till auth.user), edit profile 
    """
    user = models.OneToOneField(User, related_name='profile')
    nick = models.CharField(max_length=50)
    status = models.IntegerField(default=0, choices=STATUS)
    profile_image = models.ImageField(upload_to = 'add/', blank = True, null = True)

    def __unicode__(self):
        return unicode(self.user)
    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, **kwargs):
        Userprofile.objects.get_or_create(user=instance)
        
        
"""
(User, related_name=profile)
u = User.objects.get(id=1)
nickname = u.profile.nickname
"""