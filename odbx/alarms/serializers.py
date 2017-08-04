# -*- coding: utf-8 -*-
from rest_framework import serializers
from odbx.accounts.serializers import AccountSerializer
from odbx.alarms.models import AlarmMenu


class AlarmMenuSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField('get_user_data')

    class Meta:
        model = AlarmMenu
        fields = (
            'id', 'number', 'detect_code', 'detect_name',
            'info', 'course', 'valuation', 'user',
            'created', 'laid_time',
        )

        read_only_fields = ('number',)

    def get_user_data(self, obj):
        return AccountSerializer(obj.user).data

