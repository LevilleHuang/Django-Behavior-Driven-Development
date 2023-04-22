from django import http
from django.views.generic import View


class Home(View):

    def get(self, request: http.HttpRequest):
        return http.HttpResponse("Hello!")
