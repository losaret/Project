from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(LoginRequiredMixin, View):
    def get(self,request):
        params = {}
        params["name"] = "Django"
        return render(request, 'base.html', params)
    def post(self,request):
        return HttpResponse('Request post')