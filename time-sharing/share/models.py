from django.db import models
from userprofile.models import Userprofile
from datetime import datetime, timedelta
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust


STATUS = (
    ('A', 'Active'),
    ('E', 'Expired'),
)

class TopShare(models.Manager):
    def last_list(self):
        ad = Share.objects.all().order_by('-created')[:2]
        return ad
    # can be user like Share.objects.topshare()

class Share(models.Model):
    """
    Share: name, user, description, image, categories : Categories, name
    
    >>> s = Share()
    >>> s.title = 'Foo'
    >>> s.text = 'foo text'
    >>> s.category = Category.objects.create(name = 'maskar')
    >>> print s.text
    foo text
    >>> print s.title
    Foo
    """
    
    title = models.CharField(max_length=40)
    text = models.TextField()
    category = models.ForeignKey('Category')
    user = models.ForeignKey(Userprofile)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length=2, choices = STATUS)
    image = models.ImageField(upload_to = 'add/', blank = True, null = True)

    formatted_image = ImageSpecField(image_field='image', format='JPEG',
            options={'quality': 90})
    thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
        ResizeToFill(50, 50)], image_field='image',
        format='JPEG', options={'quality': 90})
    objects = TopShare()

    """
        
    def second_to_finish():
        created = created
        now = timedelta(microseconds=-1)
        now_s = now.seconds
        end = now_s
        
    
    
    def get_last():
        ad = Share.objects.all()order_by('-created')[:2]
        return ad
    """
    
                 
    def __unicode__(self):
        return unicode(self.user) + " : " + unicode(self.title)
    
    
    class Meta:
        ordering = ['-created', ]
                     

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name
    
    
    
    
"""
user = models.ForeignKey(Userprofile, relate_name='ads')
u = Userprofile.objects.get(id=1)
# ads = u.ad_set.all()
ads = u.ads.all()

"""