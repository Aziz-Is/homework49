from django.db import models

# Create your models here

class Status(models.Model):
    status = models.CharField(max_length=20, default='new')
    def __str__(self):
        return f'{self.status}'


class Type(models.Model):
    type = models.CharField(max_length=20, default='task')
    def __str__(self):
        return f'{self.type}'


class Tracker(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='zagolovok')
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='opisanie')
    status = models.ForeignKey(Status, related_name='tracker_status', on_delete=models.PROTECT)
    type = models.ForeignKey(Type, related_name='tracker_type', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Vremy sozdaniy')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='vremy izmeneniy')

    def __str__(self):
        return f'{self.summary}{self.updated_at}'

    class Meta:
        pass



