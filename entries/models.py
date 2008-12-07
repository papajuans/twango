import datetime
from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    user = models.ForeignKey(User)
    message = models.CharField(max_length=140)
    date_posted = models.DateTimeField(default=datetime.datetime.now)
    
    def __unicode__(self):
        return self.message
    
    class Admin:
        pass
    
    class Meta:
        verbose_name_plural = 'entries'
