from django.core.urlresolvers import reverse as django_reverse


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
    return '{}{}'.format(base_url, django_reverse(name, *args, **kwargs))
