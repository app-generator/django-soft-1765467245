# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Api_Users(models.Model):

    #__Api_Users_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    password = models.TextField(max_length=255, null=True, blank=True)
    security_token = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    account_status = models.BooleanField()
    account_age = models.TextField(max_length=255, null=True, blank=True)
    creation_location = models.TextField(max_length=255, null=True, blank=True)
    last_login_location = models.TextField(max_length=255, null=True, blank=True)

    #__Api_Users_FIELDS__END

    class Meta:
        verbose_name        = _("Api_Users")
        verbose_name_plural = _("Api_Users")


class Sys_Users(models.Model):

    #__Sys_Users_FIELDS__
    email = models.TextField(max_length=255, null=True, blank=True)
    password = models.TextField(max_length=255, null=True, blank=True)
    role = models.TextField(max_length=255, null=True, blank=True)
    security_token = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    account_status = models.BooleanField()
    account_age = models.IntegerField(null=True, blank=True)
    creation_ip = models.TextField(max_length=255, null=True, blank=True)
    creation_location = models.TextField(max_length=255, null=True, blank=True)
    last_login_location = models.TextField(max_length=255, null=True, blank=True)

    #__Sys_Users_FIELDS__END

    class Meta:
        verbose_name        = _("Sys_Users")
        verbose_name_plural = _("Sys_Users")


class Works(models.Model):

    #__Works_FIELDS__
    image = models.TextField(max_length=255, null=True, blank=True)
    title = models.TextField(max_length=255, null=True, blank=True)
    summary = models.TextField(max_length=255, null=True, blank=True)
    category = models.TextField(max_length=255, null=True, blank=True)
    link_to_work = models.TextField(max_length=255, null=True, blank=True)
    slug = models.TextField(max_length=255, null=True, blank=True)
    date_published = models.DateTimeField(blank=True, null=True, default=timezone.now)
    date_updated = models.DateTimeField(blank=True, null=True, default=timezone.now)
    publisher_name = models.ForeignKey(SYS_users, on_delete=models.CASCADE)
    publisher_ip = models.TextField(max_length=255, null=True, blank=True)
    publisher_location = models.TextField(max_length=255, null=True, blank=True)

    #__Works_FIELDS__END

    class Meta:
        verbose_name        = _("Works")
        verbose_name_plural = _("Works")


class Smpt_Messages(models.Model):

    #__Smpt_Messages_FIELDS__
    message = models.TextField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    sender_ip = models.TextField(max_length=255, null=True, blank=True)
    sender_location = models.TextField(max_length=255, null=True, blank=True)
    message_flag = models.BooleanField()
    read_flag = models.BooleanField()
    spam_flag = models.BooleanField()
    important_flag = models.BooleanField()
    thread_position = models.IntegerField(null=True, blank=True)
    recipient = models.TextField(max_length=255, null=True, blank=True)
    attachments = models.TextField(max_length=255, null=True, blank=True)

    #__Smpt_Messages_FIELDS__END

    class Meta:
        verbose_name        = _("Smpt_Messages")
        verbose_name_plural = _("Smpt_Messages")


class Page_Tracking(models.Model):

    #__Page_Tracking_FIELDS__
    user_ip = models.TextField(max_length=255, null=True, blank=True)
    page_visited = models.TextField(max_length=255, null=True, blank=True)
    onpage_duration = models.IntegerField(null=True, blank=True)
    flag = models.BooleanField()

    #__Page_Tracking_FIELDS__END

    class Meta:
        verbose_name        = _("Page_Tracking")
        verbose_name_plural = _("Page_Tracking")


class Bot_Block(models.Model):

    #__Bot_Block_FIELDS__
    reason = models.TextField(max_length=255, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    status = models.BooleanField()
    blocked_by = models.TextField(max_length=255, null=True, blank=True)
    blocker_ip = models.TextField(max_length=255, null=True, blank=True)
    blocker_location = models.TextField(max_length=255, null=True, blank=True)

    #__Bot_Block_FIELDS__END

    class Meta:
        verbose_name        = _("Bot_Block")
        verbose_name_plural = _("Bot_Block")


class Sub_Newsletter(models.Model):

    #__Sub_Newsletter_FIELDS__
    date_subscribed = models.DateTimeField(blank=True, null=True, default=timezone.now)
    sub_status = models.BooleanField()
    something = models.TextField(max_length=255, null=True, blank=True)

    #__Sub_Newsletter_FIELDS__END

    class Meta:
        verbose_name        = _("Sub_Newsletter")
        verbose_name_plural = _("Sub_Newsletter")



#__MODELS__END
