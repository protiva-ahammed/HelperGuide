from django.db import models



class Showpost(models.Model):#tablename should be upper letter
    name=models.CharField(max_length=20)
    post_name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images/')
    age=models.IntegerField(default=15)
    address=models.CharField(max_length=50)
    phn=models.CharField(max_length=20)
    experience=models.IntegerField(default=0)
    salary=models.CharField(max_length=10)
    rating=models.IntegerField(default=1)
    pub_date=models.DateTimeField()


    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    #def name(self):
    #    return self.address[:8]
    
    def __str__(self):
        return self.post_name,self.name
    
    
    def __str__(self):   #need to know how it work
        return f'{self.name} Profile'


        