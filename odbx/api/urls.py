# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url
from rest_framework_extensions.routers import ExtendedDefaultRouter as DefaultRouter
from odbx.api.views import accounts
from odbx.api.views.alarms import AlarmViewSet


router = DefaultRouter()

router.register(r'alarms', AlarmViewSet)


urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    url(r'^accounts/me/$', accounts.me),
)
