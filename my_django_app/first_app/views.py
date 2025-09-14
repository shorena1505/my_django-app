
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView


def home(request):
    return HttpResponse("Hello, Django!")

def not_found(request):
    return HttpResponse("404")


class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Home page!")

class NotFoundView(View):
    def get(self, request):
        return HttpResponse("404")