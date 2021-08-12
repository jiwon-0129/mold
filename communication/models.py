from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.utils import timezone
# Create your models here.


class Template(models.Model):
    intro = models.CharField(max_length=500, blank=True)
    contents = models.CharField(max_length=1000, blank=True)
    closing = models.CharField(max_length=500, blank=True)


class Grade(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    pub_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200, null=True)
    sending = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=100, null=True)
    test = models.CharField(max_length=100, null=True)


class Meeting(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    pub_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200, null=True)
    sending = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=50, null=True)
    background = models.CharField(max_length=500, null=True)
    time = models.CharField(max_length=100, null=True)


class Attendance(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    pub_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200, null=True)
    sending = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=100, null=True)
    evidence = models.CharField(max_length=500, null=True)
    date = models.CharField(max_length=100, null=True)


class Recommendation(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    pub_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200, null=True)
    sending = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=50, null=True)
    event = models.CharField(max_length=500, null=True)
    intro = models.CharField(max_length=100, null=True)
    detail = models.CharField(max_length=500, null=True)
