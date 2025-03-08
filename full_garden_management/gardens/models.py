from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    watering_schedule = models.CharField(max_length=100)
    fertilizer_type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
