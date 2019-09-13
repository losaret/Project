from django.conf import settings


def urlize_hashtags(text):
    """
    Converts hashtags in plain text into clickable links.
    For example, if value of ``text`` is "This is a #test.", the output will be::
      This is a
      <a href="">
          #test</a>.
    Note that if the value of ``text`` already contains HTML markup, things
    won't work as expected. Prefer use this with plain text.
    """

    url = 'http://%s/hashtag/' % (settings.SITE_HOST)
    post = []
    for word in text.split(" "):
        if word[0] == '#':
            post.append('<a href="%s">&#35;%s</a>' % (url+ word[1:], word[1:]))
        else:
            post.append(word)
    return (' ').join(post)