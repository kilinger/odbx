# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from odbx.accounts.models import DlStaffInfo
from odbx.accounts.serializers import AccountSerializer
from odbx.accounts.filters import DlStaffInfoFilter


@api_view(['GET', 'OPTIONS'])
def me(request):
    serializer = AccountSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)
