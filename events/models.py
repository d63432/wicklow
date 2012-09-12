from django.db import models

class Conference(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return self.name
