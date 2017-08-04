# -*- coding:utf-8 -*-
from rest_framework import viewsets
from odbx.alarms.filters import AlarmMenuFilter
from odbx.alarms.models import AlarmMenu
from odbx.alarms.serializers import AlarmMenuSerializer


class AlarmViewSet(viewsets.ModelViewSet):
    queryset = AlarmMenu.objects.all()
    serializer_class = AlarmMenuSerializer
    filter_class = AlarmMenuFilter

    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options', 'trace']

    def perform_create(self, serializer):
        """
        :type serializer: `odbx.alarms.serializers.AlarmMenuSerializer`
        :return:
        """
        serializer.initial_data.pop('course', None)
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """
        :type serializer: `odbx.alarms.serializers.AlarmMenuSerializer`
        :return:
        """
        new_course = serializer.initial_data.get('course', None)
        if not serializer.instance.allow_update_course(new_course, self.request.user):
            serializer.initial_data.pop('course', None)
        if not serializer.instance.allow_update_valuation(self.request.user):
            serializer.initial_data.pop('valuation', None)
        serializer.save()
