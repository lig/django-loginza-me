from distutils.core import setup


setup(
    name='django-loginza-me',
    version='0.1.dev0',
    author='Serge Matveenko',
    author_email='s@matveenko.ru',
    description='Django app and auth backend for authenticating using'
        'http://loginza.ru/ service.',
    url='https://github.com/lig/django-loginza-me',
    license='Public Domain',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: Public Domain',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Programming Language :: Python :: 2',
        'Framework :: Django',
    ],
    packages=['loginza'],
    requires=['Django (<1.4)', 'mongoengine'],
)
