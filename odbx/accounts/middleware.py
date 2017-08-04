# -*- coding: utf-8 -*-
from django.http import Http404


class UserAccessControl(object):
    def process_request(self, request):

        if request.path == '/api/':
            raise Http404
        user = request.user
        if not user.is_authenticated():
            return
