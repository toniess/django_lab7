from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    id = models.Count

    def __unicode__(self):
        return "%s: %s" % (self.author, self.title)

    def get_excerpt(self):
        if len(self.text) > 240:
            return self.text[:240] + "..."
        else:
            return self.text
