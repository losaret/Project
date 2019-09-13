from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import blog_post


class Index(LoginRequiredMixin, View):
    def get(self,request):
        params = {}
        params["name"] = "Django"
        return render(request, 'base.html', params)
    def post(self,request):
        return HttpResponse('Request post')

class Profile(View):
    """User profile reachable from /user/<username> URL"""
    def get(self, requset, username):
        params = dict()
        params['posts'] = blog_post.objects.filter(user=user)
        params['user'] = User.objects.get(username=username)
        return render(request, 'blog_site/other_profile.html', params)