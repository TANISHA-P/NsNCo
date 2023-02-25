from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Client(models.Model):
    Name = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"Client {self.Name}"

work_choices = (
    ('yt','Youtube'),
    ('ig','Instagram'),
    ('other','Other')
)
class Work(models.Model):
    work_type = models.CharField(choices=work_choices,default='Youtube',max_length=20)
    link = models.URLField()

    def __str__(self):
        return f"Work {self.work_type}"

class Artist(models.Model):
    Name = models.OneToOneField(Client,on_delete=models.CASCADE)
    work = models.ManyToManyField(Work)

    def __str__(self):
        return f"Artist {self.Name.Name}"