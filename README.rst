loaderio-django
===============

A Django app that makes it easy to validate your site against loader.io.

Quickstart
----------

1. Add "loaderio" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'loaderio',
    )

2. Include the loaderio URLconf in your project urls.py like this::

    url('^$', include('loaderio.urls'))

3. Run `python manage.py migrate` to create the loaderio models.

4. Visit /admin/loaderio to add loader.io validation tokens.
