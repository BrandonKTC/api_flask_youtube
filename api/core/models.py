from django.db import models

# Create your models here.
class User(models.Model):
 user_id = models.AutoField(primary_key=True)
 pseudo = models.CharField(max_length=45)
 username = models.CharField(max_length=45,unique=True)
 email = models.EmailField(unique=True)
 password = models.CharField(max_length=45)

 def __str__(self):
  return "Recipe for {}".format(self.username)

class Video(models.Model):
 QUALITY = (
  ('1080','1080'),
  ('720','720'),
  ('480','480'),
  ('360','360'),
  ('240','240'),
 )
 video_id = models.AutoField(primary_key=True)
 name = models.CharField(max_length=45, unique=True)
 duration = models.PositiveIntegerField()
 user_id = models.ForeignKey(User, on_delete=models.CASCADE)
 source = models.FileField()
 quality = models.CharField(choices=QUALITY, max_length=10)
 created_at = models.DateField(auto_now_add=True)

 def __str__(self):
  return "Recipe for {}".format(self.name)