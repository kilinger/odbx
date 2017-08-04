# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers
from odbx.accounts.models import DlStaffInfo


class AccountSerializer(serializers.ModelSerializer):

    post = serializers.SerializerMethodField('get_post_data')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'post')

    def get_post_data(self, obj):
        info = DlStaffInfo.objects.get_or_create(user=obj)[0]
        return info.post
