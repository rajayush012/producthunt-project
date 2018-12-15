from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    url = models.TextField()
    votes_total=models.PositiveIntegerField(default=1)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[0:106]+"..."

    def pub_date_pre(self):
        return self.pub_date.strftime("%b %e %Y")

    def __str__(self):
        return self.title
