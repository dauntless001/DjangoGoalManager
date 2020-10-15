from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    duration = models.CharField(max_length=4, help_text='Convert to Days')
    slug = models.SlugField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if self.slug is None and self.name:
            from django.utils.text import slugify
            self.slug = slugify(self.name + str(timezone.now()))
        return super(Goal, self).save(args, kwargs)
    
    def get_absolute_url(self):
        from django.shortcuts import reverse
        return reverse('goal:detail', kwargs={'slug':self.slug})


class Objective(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    obj = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='objectives')
    comment = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    completed = models.BooleanField(default=False)


    class Meta:
        ordering = ['comment']
    def __str__(self):
        return self.comment
    
    
    def save(self, *args, **kwargs):
        if self.slug is None:
            from django.utils.text import slugify
            self.slug = slugify(self.comment)
        return super(Objective, self).save(args, kwargs)
    