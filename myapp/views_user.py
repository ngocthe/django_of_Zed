# myapp/views_user.py
import os.path
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.shortcuts import render, redirect
from . import models


def sw_list(request):
    try:
        empList = models.SWMember.objects.all().order_by('userID')
        return render(request, 'myapp/sw_list.html', {'empList': empList})
    except Http404:
        return HttpResponseBadRequest()


def add_new_member(request):
    try:
        return render(request, 'myapp/add_new_member.html')
    except Http404:
        return HttpResponseBadRequest()