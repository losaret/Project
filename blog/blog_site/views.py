from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import blog_post, Hashtag
from .forms import PublishForm


class Index(LoginRequiredMixin, View):
    """ Index page reachable from / URL"""
    def get(self,request):
        params = dict()
        userProfile = User.objects.get(username=request.user.username)     
        params['form'] = PublishForm()
        return render(request, 'blog_site/self_profile.html', params)

class Profile(View):
    """User profile reachable from /user/<username> URL"""
    def get(self, request, username):
        params = dict()
        userProfile = User.objects.get(username=username)
        params['posts'] = blog_post.objects.filter(user=userProfile)
        params['user'] = User.objects.get(username=username)
        return render(request, 'blog_site/other_profile.html', params)

class Publishpost(View):
    """Publish post from available on page / URL"""
    def post(self, request):
        form = PublishForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            text = form.cleaned_data['text']
            published_post = blog_post(
                post_text = text,
                user = user
            )
            published_post.save()
            words = form.cleaned_data['text'].split(' ')
            for word in words:
                if word[0] == '#':
                    Add_Hashtag, created = Hashtag.objects.get_or_create(name=word[1:])
                    Add_Hashtag.post.add(published_post)
        return HttpResponseRedirect('/')

class HastagCloud(View):
    """ Hashtag page reachable from /hashtag/<hashtag> URL"""
    def get(self, request, hashtag):
        params = dict()
        get_hashtag = Hashtag.objects.get(name=hashtag)
        params['posts'] = get_hashtag.post
        return render(request, 'blog_site/hashtag.html', params)