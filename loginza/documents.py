from django.contrib.auth.models import UNUSABLE_PASSWORD
from mongoengine import Document, StringField, ReferenceField, DictField
from mongoengine.django.auth import User

# monkey patching User to be able to store long identities
User.username.max_length = None


__all__ = ['Identity']


class Identity(Document):

    identity = StringField(primary_key=True)
    user = ReferenceField(User)
    info = DictField()

    def __unicode__(self):
        return u'%s (%s)' % (self.user, self.info_json)

    @classmethod
    def get_or_create(cls, loginza_response):

        identity_qs = cls.objects.filter(identity=loginza_response['identity'])

        if identity_qs.count():
            identity = identity_qs.get()
        else:
            user_qs = User.objects.filter(
                username=loginza_response['identity'])

            if user_qs.count():
                user = user_qs.get()
            else:
                user = User.create_user(
                    username=loginza_response['identity'],
                    password=UNUSABLE_PASSWORD,
                    email=loginza_response.get('email'))

            identity = Identity(identity=loginza_response['identity'],
                user=user)

        del loginza_response['identity']
        identity.info = loginza_response

        identity.save()

        return identity
