from django.db import models
from userprofile.models import Userprofile
from datetime import datetime
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust

STATUS = (
    ('A', 'Active'),
    ('E', 'Expired'),
)

class Share(models.Model):
    """
    Share: name, user, description, image, categories : Categories, name
    
    """
    title = models.CharField(max_length=30)
    text = models.TextField()
    category = models.ForeignKey('Category')
    user = models.ForeignKey(Userprofile)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length=2, choices = STATUS)
    image = models.ImageField(upload_to = 'add/')
    formatted_image = ImageSpecField(image_field='image', format='JPEG',
            options={'quality': 90})
    thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
        ResizeToFill(50, 50)], image_field='image',
        format='JPEG', options={'quality': 90})

    def __unicode__(self):
        return unicode(self.user) + " : " + unicode(self.title)
    
class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name
    