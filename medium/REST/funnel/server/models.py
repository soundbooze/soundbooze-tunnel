from django.db import models

# Create your models here.
class Server(models.Model):
    ipaddress = models.CharField(max_length=15)
 
    class Meta:
        verbose_name = "Server"
        verbose_name_plural = "Servers"
 
    def __unicode__(self):
        return self.name
