# from django.db import models

# class UploadedImage(models.Model):
#     image = models.ImageField(upload_to='uploads/')


from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')

class Meta:
    app_label = 'imageapp'