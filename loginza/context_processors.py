from django.core.urlresolvers import reverse


def loginza_url(request):
    return {'LOGINZA_URL': 'http://%s:%s%s' % (request.META['SERVER_NAME'],
        request.META['SERVER_PORT'], reverse('loginza-login'))}
