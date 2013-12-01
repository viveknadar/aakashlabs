from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coordinator(models.Model):
    """Aakash Coordinators.
    """
    user = models.OneToOneField(User)

    # Addition info
    contact = models.IntegerField(max_length=12, blank=True)
    picture = models.ImageField(upload_to='profile_image', blank=True)

    def __unicode__(self):
        return self.user.username

        
class RemoteCenter(models.Model):
    """Remote centers.
    """
    rc_id = models.IntegerField(max_length=4, unique=True)
    name = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    coordinator = models.OneToOneField(User)
    status = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name


        
        
        
