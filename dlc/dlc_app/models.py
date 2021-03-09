from django.db import models


class Foods(models.Model):
    image = models.ImageField(upload_to="news_image", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at}"


class Comment(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    subject = models.CharField(max_length=50, null=False, blank=False, default='kkuh')
    email = models.EmailField(null=False, blank=False,default='sayfififid@gmail.com')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Recept(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to="news_image", null=True)

    def __str__(self):
        return f"{self.name}"

