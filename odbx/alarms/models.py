# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from model_utils import Choices
from django.utils import timezone


def gen_alarm_number():
    time = timezone.now() + datetime.timedelta(hours=8)
    time_str = time.strftime('%Y%m%d%H%M%S')
    return time_str


@python_2_unicode_compatible
class AlarmMenu(models.Model):

    STATUS_CHOICES = Choices(
        ('1', _(u"未审核")),
        ('2', _(u"审核不通过")),
        ('3', _(u"待维修")),
        ('4', _(u"维修中")),
        ('5', _(u"已完成")),
        ('6', _(u"已评价")),

    )

    created = models.DateTimeField(auto_now_add=True, help_text=_(u"报修时间"))
    laid_time = models.DateTimeField(auto_now_add=True, help_text=_(u"入库时间"))
    number = models.CharField(max_length=20, default=gen_alarm_number, help_text=_(u"报修单号"))
    detect_code = models.CharField(max_length=20, help_text=_(u"报修材料编码"))
    detect_name = models.CharField(max_length=40, help_text=_(u"报修材料名称"))
    user = models.ForeignKey(User, help_text=_(u"报修人员"))
    info = models.CharField(max_length=100, help_text=_(u"报修原因"))
    course = models.CharField(choices=STATUS_CHOICES, default='1', max_length=1, help_text=_(u"报修进度"))
    valuation = models.CharField(max_length=40, blank=True, help_text=_(u"报修评价"))

    class Meta:
        verbose_name = _(u"工单")
        verbose_name_plural = _(u"工单")
        ordering = ('-created', )

    def __str__(self):
        return "{0}".format(self.user)

    def allow_update_course(self, new_course, user):
        try:
            post = int(user.staff.post)
            new_course = int(new_course)
            course = int(self.course)
        except ValueError:
            return False

        if new_course == 1 or course == 2:
            return False

        if course == 1 and new_course == 3 and post == 1:
            return True

        if course + 1 == new_course and post == 2:
            return True

        return False

    def allow_update_valuation(self, user):
        try:
            post = int(user.staff.post)
        except ValueError:
            return False

        if self.user == user and post == 3 and not self.valuation:
            return True
        return False