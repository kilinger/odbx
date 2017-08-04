# -*- coding:utf-8 -*-
from django.contrib import admin
from odbx.alarms.models import AlarmMenu


class AlarmMenuAdmin(admin.ModelAdmin):
    search_fields = ['number']
    list_display = ('number', 'user')
    list_filter = ('created',)


admin.site.register(AlarmMenu, AlarmMenuAdmin)
