from datetime import datetime
from json import load
from urllib2 import urlopen

from mongoengine.django.auth import User

from ..models import Identity


class LoginzaException(Exception):

    def __init__(self, error_type, error_message):
        self.raised = datetime.now().isoformat()
        self.error_type = error_type
        self.error_message = error_message

    def __repr(self):
        return u'%s loginza: %s: %s' % (self.raised, self.error_type,
            self.error_message)


class LoginzaBackend(object):

    def authenticate(self, token):

        loginza = urlopen('http://loginza.ru/api/authinfo?token=%s' % token)

        loginza_response = load(loginza)

        if 'error_type' in loginza_response:
            raise LoginzaException(loginza_response['error_type'],
                loginza_response['error_message'])
        else:
            identity = Identity.get_or_create(loginza_response)

        return identity.user

    def get_user(self, user_id):
        user = User.objects.get(pk=user_id)
        identity_qs = Identity.objects.filter(pk=user.username)
        if identity_qs.exists():
            identity = Identity.objects.get(pk=user.username)
            user.info = identity.info
            return user
