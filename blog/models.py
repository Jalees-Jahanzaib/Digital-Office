from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.urls import reverse
# Create your models here.
class Files(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
    ('S', 'Scan'),
    ('1', 'Phase 1'),
    ('2', 'Phase 2'),
    ('3', 'Phase 3'),
    ('F', 'Final'),
]
    title=models.CharField(max_length=100)
    summary=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    Roles=models.CharField(max_length=10,choices=YEAR_IN_SCHOOL_CHOICES,default='Scan')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('file-detail', kwargs={ 'pk' : self.pk} )

        
    

