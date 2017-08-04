# -*- coding:utf-8 -*-
import django_filters
from odbx.alarms.models import AlarmMenu


class AlarmMenuFilter(django_filters.FilterSet):

    post = django_filters.CharFilter(name="user__staff__post")
    username = django_filters.CharFilter(name="user__username")
    since_id = django_filters.CharFilter(name="id", lookup_type="lt")
    max_id = django_filters.CharFilter(name="id", lookup_type="gt")
    course = django_filters.CharFilter(name="course", lookup_type="gt")

    class Meta:
        model = AlarmMenu
        fields = ("post", "username", "course", "since_id", "max_id", "number")
