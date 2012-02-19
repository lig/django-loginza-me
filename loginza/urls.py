from django.conf.urls.defaults import patterns


urlpatterns = patterns('%s.views' % __package__,
    (r'^login/$', 'loginza_complete', {}, 'loginza-login'),
    (r'^logout/$', 'loginza_logout', {}, 'loginza-logout'),
)
