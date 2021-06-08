from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    #Userと一対一対応
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics") #保管場所

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self): #小さな画像にするために変更
        super().save()
        img =Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

