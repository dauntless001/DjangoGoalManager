from django.db import models
import datetime
from django.conf import settings
# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.CharField(max_length=25)
    slug = models.SlugField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['task']

    def __str__(self):
        return self.task

    def save(self, *args, **kwargs):
        if self.slug is None and self.task:
            from django.utils.text import slugify
            from django.utils import timezone
            self.slug = slugify(self.task+str(timezone.now()))
        return super(Todo, self).save(args, kwargs)
    