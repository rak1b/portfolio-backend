from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project/',default="project/default.png", blank=True, null=True)
    live_url = models.CharField(max_length=500, blank=True, null=True)
    code_url = models.CharField(max_length=500, blank=True, null=True)
    tags = models.CharField(max_length=500, blank=True, null=True)

    @property
    def tags_list(self):
        return self.tags.split(',')

    def __str__(self):
        return self.name
