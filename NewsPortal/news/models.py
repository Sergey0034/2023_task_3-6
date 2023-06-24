from django.db import models


class New(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)