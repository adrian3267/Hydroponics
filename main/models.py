from django.db import models

class PageContent(models.Model):
    field_name = models.CharField(max_length=50)
    english = models.CharField(max_length=1000, default='')
    chinese = models.CharField(max_length=1000, default='')
    italian = models.CharField(max_length=1000, default='')
    portuguese = models.CharField(max_length=1000, default='')
    slovak = models.CharField(max_length=1000, default='')
    spanish = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.field_name