import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    # models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
    

post_save.connect(create_profile, sender=User)


class Static8FModel(models.Model):
    LGesamt   = models.FloatField(default=0.0)
    LSammler  = models.FloatField(default=0.0)
    Fabstand1 = models.FloatField(default=0.0)
    Fabstand2 = models.FloatField(default=0.0)
    Fabstand3 = models.FloatField(default=0.0)

    mLeer     = models.FloatField(default=0.0)
    mSammler  = models.FloatField(default=0.0)
    VRohr     = models.FloatField(default=0.0)

    F12Leer   = models.FloatField(default=0.0)
    F34Leer   = models.FloatField(default=0.0)
    F56Leer   = models.FloatField(default=0.0)
    F78Leer   = models.FloatField(default=0.0)

    F12Voll   = models.FloatField(default=0.0)
    F34Voll   = models.FloatField(default=0.0)
    F56Voll   = models.FloatField(default=0.0)
    F78Voll   = models.FloatField(default=0.0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Static6FModel(models.Model):
    LGesamt   = models.FloatField(default=0.0)
    LSammler  = models.FloatField(default=0.0)
    Fabstand1 = models.FloatField(default=0.0)
    Fabstand2 = models.FloatField(default=0.0)

    mLeer     = models.FloatField(default=0.0)
    mSammler  = models.FloatField(default=0.0)
    VRohr     = models.FloatField(default=0.0)

    F12Leer   = models.FloatField(default=0.0)
    F34Leer   = models.FloatField(default=0.0)
    F56Leer   = models.FloatField(default=0.0)


    F12Voll   = models.FloatField(default=0.0)
    F34Voll   = models.FloatField(default=0.0)
    F56Voll   = models.FloatField(default=0.0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)