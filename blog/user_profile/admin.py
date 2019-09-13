from django.contrib import admin
from .models import UserFollower, UserFollowing
# Register your models here.


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user', )

admin.site.register(UserFollower, FollowAdmin)
admin.site.register(UserFollowing, FollowAdmin)