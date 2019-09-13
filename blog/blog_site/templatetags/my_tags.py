from blog_site.utils import urlize_hashtags
from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

def with_hashtags(value):
    return urlize_hashtags(value)

with_hashtags.is_safe = True
with_hashtags = stringfilter(with_hashtags)
register.filter(with_hashtags)