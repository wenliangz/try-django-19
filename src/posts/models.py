from django.db import models
from django.core.urlresolvers import reverse
from django.conf import  settings

# Create your models here.
def upload_location(instance, filename):
    # filebase,extension = filename.split('.')
    return '%s/%s'%(instance.id,filename)
    # return '%s/%s.%s'%(instance.id,instance.id,extension)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=False)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              height_field='height_field',
                              width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail',kwargs={'id':self.id})
        # return '/posts/%s'%(self.id)

    class Meta:
        ordering = ['-timestamp','-updated']