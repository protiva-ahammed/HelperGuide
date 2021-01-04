from django.db import models
from django.contrib.auth.models import User
from django.core.files import File


class Electrician(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    #nid=models.CharField(max_length)
    experience=models.CharField(max_length=20)
    esalary=models.CharField(max_length=20)
    contract=models.CharField(max_length=20)
    address=models.CharField(max_length=150)
    votes_total=models.IntegerField(default=1)
    skill=models.CharField(max_length=150)
    url = models.CharField(max_length=50)
    #cv= models.FileField(upload_to='documents/')
    image= models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    seeker = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title,self.seeker

    def des(self):
        return self.description[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def save(self, *args, **kwargs):
        super().save()