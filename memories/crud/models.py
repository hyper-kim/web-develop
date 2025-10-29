from django.db import models

# Create your models here.
class Addmemory(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user_tag = models.TextField(null=True,blank=True)
    hash_tag = models.TextField()
    username = models.CharField(max_length=255)
    like = models.IntegerField()
    report = models.IntegerField()
    def __str__(self):
        return str(self.title)
    def summary(self):
        return self.body[:50]

class Photo(models.Model):
    post = models.ForeignKey(Addmemory, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)