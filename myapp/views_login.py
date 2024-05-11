import os.path
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import models
from . import forms


@require_http_methods(["POST","GET"])
def login_view(request):
    try:
        if request.method == 'POST':
            username = str.upper(request.POST.get('userID'))
            password = request.POST.get('userPW')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page or any other page after successful login
            else:
                messages.error(request, 'Invalid username or password.')
        return render(request, 'myapp/login.html')
    except Exception as e:
        print(e)
        return HttpResponseBadRequest("Bad Request Message")


def logout_view(request):
    try:
        logout(request)
        return redirect('login')
    except Http404:
        return HttpResponseBadRequest()


def test_view(request):
    try:
        return render(request, 'myapp/test.html')
    except Http404:
        return HttpResponseBadRequest()


def home_view(request):
    try:
        return render(request, 'myapp/home.html')
    except Http404:
        return HttpResponseBadRequest()
