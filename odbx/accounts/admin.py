# -*- coding:utf-8 -*-
from django.contrib import admin
from odbx.accounts.models import DlStaffInfo


class DlStaffInfoAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ('user', 'post')
    list_filter = ('post',)


admin.site.register(DlStaffInfo, DlStaffInfoAdmin)
