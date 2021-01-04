from django.db import models
from django.contrib.auth.models import User
from django.core.files import File

class Createjob(models.Model):
    title = models.CharField(max_length=20)
    duration=models.IntegerField()
    salary=models.CharField(max_length=20)
    contract=models.CharField(max_length=11)
    address=models.CharField(max_length=30)
    votes_total=models.IntegerField(default=1)
    description=models.CharField(max_length=150)
    url = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    hunter = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title,self.hunter

    def des(self):
        return self.description[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def save(self, *args, **kwargs):
        super().save()