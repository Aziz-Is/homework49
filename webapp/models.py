from django.db import models

# Create your models here.

class Tracker(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='zagolovok')
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='opisanie')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Vremy sozdaniy')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='vremy izmeneniy')

    def __str__(self):
        return f'{self.summary}{self.updated_at}'

    class Meta:
        pass

    class Status:
        pass

    class Type:
        pass


