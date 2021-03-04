from django.db import models


class Foods(models.Model):
    image = models.ImageField(upload_to="news_image",null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at}"
