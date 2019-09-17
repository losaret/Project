import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import blog_post, Hashtag
from .forms import PublishForm
from user_profile.models import UserFollower, UserFollowing


class Index(LoginRequiredMixin, View):
    """ Index page reachable from / URL"""
    def get(self,request):
        params = dict()
        userprofile = User.objects.get(username=request.user.username)
        query = Q(user=userprofile)   
        if UserFollowing.objects.filter(user=userprofile).exists():
            userfollowing = UserFollowing.objects.get(user=userprofile)
            queries = [Q(user=following) for following in userfollowing.followings.all()]
            for item in queries:
                query |= item
        posts = blog_post.objects.filter(query).order_by('-created_date')
        params['posts'] = posts
        params['profile'] = userprofile
        params['form'] = PublishForm()
        return render(request, 'blog_site/self_profile.html', params)

class Profile(View):
    """User profile reachable from /user/<username> URL"""
    def get(self, request, username):
        params = dict()
        userProfile = User.objects.get(username=username)
        try:
            userFollower = UserFollower.objects.get(user=userProfile)
            if userFollower.followers.filter(username=request.user.username).exists():
                params['following'] = True
            else:
                params['following'] = False
        except:
            params['following'] = False
            userFollower=[]
        params['posts'] = blog_post.objects.filter(user=userProfile).order_by('-created_date')
        params['profile'] = userProfile
        params['user'] = User.objects.get(username=request.user.username)
        return render(request, 'blog_site/other_profile.html', params)
    
    def post(self, request, username):
        follow = request.POST['follow']
        user = User.objects.get(username=request.user.username)
        userprofile = User.objects.get(username=username)
        userfollower, status = UserFollower.objects.get_or_create(user=userprofile)
        userfollowing, status = UserFollowing.objects.get_or_create(user=user)
        if follow == "true":
            userfollower.followers.add(user)
            userfollowing.followings.add(userprofile)
            userfollower.save()
            userfollowing.save()
        else:
            userfollower.followers.remove(user)
            userfollowing.followings.remove(userprofile)
            userfollower.save()
            userfollowing.save()
        return HttpResponse(json.dumps(''), content_type='application/json')
    

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

class Search(View):
    """ Searching posts reachable from from /search/?q=<query> URL """
    def get(self, request):
        query = request.GET.get('query')
        if query == '':
            query = None
        params = dict()
        try:
            posts = blog_post.objects.filter(post_text__icontains=query)
            params['posts'] = posts
        except ValueError:
            pass
        return render(request, 'blog_site/search.html', params)