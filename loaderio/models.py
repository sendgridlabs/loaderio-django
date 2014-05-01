from django.db import models


class Validation(models.Model):
    token = models.CharField(max_length=50)

    def __unicode__(self):
        return self.token
