# -*- coding:utf-8 -*-
import django_filters
from odbx.accounts.models import DlStaffInfo


class DlStaffInfoFilter(django_filters.FilterSet):

    post = django_filters.CharFilter(name="post")
    username = django_filters.CharFilter(name="user__username")

    class Meta:
        model = DlStaffInfo
