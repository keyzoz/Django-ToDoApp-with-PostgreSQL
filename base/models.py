from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200,null=True,blank=False)
    description = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
          return reverse('task:detail', kwargs={'pk': self.pk})
          
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']
        
    