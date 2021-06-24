import uuid
from datetime import datetime, timedelta
from django.db import models
from hashlib import md5


class Url(models.Model):
    url_full = models.URLField()
    url_hash = models.CharField(unique=True, blank=True, null=True, max_length=50)
    expired_at = models.DateTimeField(default=datetime.now() + timedelta(days=7))

    class Meta:
        verbose_name = "Url"
        verbose_name_plural = "Urls"

    def __str__(self):
        return self.url_hash

    def save(self, *args, **kwargs):
        try:
            if self.url_hash:
                if Url.objects.filter(url_hash=self.url_hash).exists():
                    self.url_hash = self.url_hash     
            else:
                self.url_hash = md5(str(uuid.uuid4()).encode()).hexdigest()[0:8]
        except Exception as exp:
            self.url_hash = md5(str(uuid.uuid4()).encode()).hexdigest()[0:8]

        super(Url, self).save(*args, **kwargs)
