# -*- coding: utf-8 -*-
import logging
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from model_utils import Choices


logger = logging.getLogger(__name__)


@python_2_unicode_compatible
class DlStaffInfo(models.Model):
    POST_STATE = Choices(
        ('1', _(u"领导")),
        ('2', _(u"维修员工")),
        ('3', _(u"客户")),
    )

    user = models.OneToOneField(User, related_name='staff')
    post = models.CharField(max_length=1, choices=POST_STATE, blank=True, null=True, help_text=_(u"角色"))

    class Meta:
        verbose_name = _(u"身份")
        verbose_name_plural = _(u"身份")
        ordering = ('-id', )

    def __str__(self):
        return "{0}".format(self.user)


@receiver(post_save, sender=User, dispatch_uid='user_save')
def _on_user_save(sender, instance, created, **kwargs):
    if instance:
        try:
            DlStaffInfo.objects.get_or_create(user=instance)
        except IOError, e:
            logger.error(str(e))
            pass