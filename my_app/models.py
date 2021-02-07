from django.db import models

# Create your models here.
class item_model(models.Model):
    title = models.CharField(max_length=250)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
    