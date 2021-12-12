from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.



class post(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    body=models.TextField()
    image1=models.ImageField(upload_to='images/')
    body2=models.TextField()
    image2=models.ImageField(upload_to='images/')
    body3=models.TextField()
    image3=models.ImageField(upload_to='images/')
    time=models.DateTimeField(timezone.now())


    def __str__(self):
        return self.title + " | " + str(self.author)
        
    class Meta:
        db_table = 'post'
        

    
    
class About(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    time=models.DateTimeField(timezone.now())
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title + " | " + str(self.author)
        
    def short_info(self):
        return self.body[:500] + '...'
        
        
 



class Proj_achievements(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    time=models.DateTimeField()
    image=models.ImageField(upload_to='images/', blank=True)
    image1=models.ImageField(upload_to='images/', blank=True)
    image1b=models.ImageField(upload_to='images/', blank=True)
    body1=models.TextField(blank=True)
    image2=models.ImageField(upload_to='images/', blank=True)
    image2b=models.ImageField(upload_to='images/', blank=True)
    body2=models.TextField(blank=True)
    image3=models.ImageField(upload_to='images/', blank=True)
    body3=models.TextField(blank=True)
    image4=models.ImageField(upload_to='images/', blank=True)
    body4=models.TextField(blank=True)
    pro_video=models.FileField(upload_to='videos/project/', blank=True)
    
    def __str__(self):
        return self.title + " | " + str(self.author)
        
    def pos(self):
        return self.body[:50] + "..."
        
class Legislative_activitie(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    time=models.DateTimeField(timezone.now())
    image=models.ImageField(upload_to='images/',blank=True)
    
    image1=models.ImageField(upload_to='images/',blank=True)
    image1b=models.ImageField(upload_to='images/',blank=True)
    body1=models.TextField(blank=True)
    
    image2=models.ImageField(upload_to='images/',blank=True)
    image2b=models.ImageField(upload_to='images/',blank=True)
    body2=models.TextField(blank=True)
    
    image3=models.ImageField(upload_to='images/',blank=True)
    body3=models.TextField(blank=True)
    
    image4=models.ImageField(upload_to='images/',blank=True)
    body4=models.TextField(blank=True)
    pro_video=models.FileField(upload_to='videos/bill/',blank=True)

    def __str__(self):
        return self.title + " | " + str(self.author)
        
    def pos(self):
        return self.body[:50] + "..."
        
class Quotes(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    time=models.DateTimeField(timezone.now())
    image=models.ImageField(upload_to='images/quotes/',blank=True)
    

    def __str__(self):
        return self.body[:20] +"..."+ " | " + str(self.author)
        
        
class Empowerment(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    time=models.DateTimeField(timezone.now())
    image=models.ImageField(upload_to='images/',blank=True)
    image1=models.ImageField(upload_to='images/',blank=True)
    image1b=models.ImageField(upload_to='images/',blank=True)
    body1=models.TextField(blank=True)
    
    image2=models.ImageField(upload_to='images/',blank=True)
    image2b=models.ImageField(upload_to='images/',blank=True)
    body2=models.TextField(blank=True)
    
    image3=models.ImageField(upload_to='images/',blank=True)
    body3=models.TextField(blank=True)
    
    image4=models.ImageField(upload_to='images/',blank=True)
    body4=models.TextField(blank=True)
    
    video_emp=models.FileField(upload_to='Video/empowerment/',blank=True)
    

    def __str__(self):
        return self.title + " | " + str(self.author)
        
    def pos(self):
        return self.body[:50] + "..."

class contact_message(models.Model):
	name=models.CharField(max_length=200)
	message=models.TextField()
	
class image(models.Model):
    img=models.ImageField(upload_to='images/', blank=True)
    img1=models.ImageField(upload_to='images/', blank=True)
    img2=models.ImageField(upload_to='images/', blank=True)
    time=models.DateTimeField(timezone.now())

