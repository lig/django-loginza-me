# About

django-loginza-me is the Django app and auth backend for authenticating using http://loginza.ru/ service.


# Usage

## settings.py

    INSTALLED_APPS = (
        # …
        'django.contrib.auth',
        # …
        'loginza',
        # …
    )

    from django.conf.global_settings import (TEMPLATE_CONTEXT_PROCESSORS,
        AUTHENTICATION_BACKENDS)
    
    TEMPLATE_CONTEXT_PROCESSORS += (
        'loginza.context_processors.loginza_url',
    )
    
    AUTHENTICATION_BACKENDS += (
        'loginza.auth.backends.LoginzaBackend',
    )
    LOGIN_URL = '/'  # or any page you will display login form on
    LOGIN_REDIRECT_URL = '/'  # or any page you want to redirect user after login to
    LOGOUT_URL = '/'  # or any page you want to redirect user after logout to

## urls.py

    urlpatterns = patterns('',
        # …
        url(r'^auth/', include('loginza.urls')),
        # …
    )

## Templates

* Get widget code at [Loginza](http://loginza.ru/). 
* Use `{{ LOGINZA_URL }}` as `token_url` widget parameter.
* Use `{% url loginza-logout %}` for logout link url.
