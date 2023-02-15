from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) #here we have used a OneToOneField rather than a Foreign Key for the following reasons: (1) If a foreign key is joining two models (say A and B), then A gives uniques B output, but same B's value may give many A output. Eg, Roll no. 10(A) is from class 8th(B), but there are many roll no.s in class 8th.
    #(2) This problems is solved in OneToOneField. Here, every A field gives unique B field's value and vice-versa.  
    image = models.ImageField(default='default.jpg', upload_to='xx/profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
class Temp(models.Model):
    image2 = models.ImageField(default="default.jpg", upload_to='xx/profile_pics2')
    