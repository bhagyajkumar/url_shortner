from django.db import models
import string
import random
import re

from django.core.exceptions import ValidationError

def generate_key():
    # generate a random key of length 5 which is not in the database
    while True:
        key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        if not Url.objects.filter(key=key).exists():
            break
    return key

def validate_url(value):
    regex = re.compile("^http[s]?:\/\/(www\.)?(.*)?\/?(.)*")
    if not regex.match(value):
        raise ValidationError(
            _('%(value)s is not a valid URL'),
            params={'value': value},
        )
            



class Url(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=20, unique=True, default=generate_key)
    url = models.URLField(max_length=200, null=False, blank=False , validators=[validate_url])
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='urls',on_delete=models.SET_NULL, null=True, blank=True, default=None)
    clicks = models.IntegerField(default=0)


    def __str__(self):
        return self.key
