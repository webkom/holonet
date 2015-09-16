from django.core import urlresolvers


def base_url(request):
    """
    Return base_url
    """
    if request.is_secure():
        scheme = 'https://'
    else:
        scheme = 'http://'

    return scheme + request.get_host()


def reverse(name, base_url, *args, **kwargs):
    return '{}{}'.format(base_url, urlresolvers.reverse(name, *args, **kwargs))
