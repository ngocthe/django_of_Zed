# middleware_sample/middlewares.py
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        print("starting middleware: ", request.user.is_authenticated)
        print("request.path", request.path)
        if not request.path.startswith('/admin/'):
            if not request.user.is_authenticated and request.path != reverse('login'):
                print("going to index middleware: {}", request.user.is_authenticated)
                return redirect('login')
        if request.path.startswith('/admin/'):
            response = HttpResponseRedirect(reverse('admin:index'))
        else:
            response = self.get_response(request)
        print("ending middleware", request.user.is_authenticated)
        return response

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        pass
