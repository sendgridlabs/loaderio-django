loaderio-django
===============

A Django app that makes it easy to verify your application against loader.io_ by
allowing you to specify your loader.io `verification token`_ in the Django admin
interface.

.. _loader.io: https://loader.io
.. _verification token: http://support.loader.io/article/20-verifying-an-app


Installation
------------

1. Add "loaderio" to your INSTALLED_APPS in your Django settings::

    INSTALLED_APPS = (
        ...
        'loaderio',
    )

2. Include the loaderio URLconf in your project urls.py::

    url('^$', include('loaderio.urls'))

3. Update your database schema with the new models::

        python manage.py syncdb

Usage
-----

Once installed, the admin interface will have a *Loaderio* section with
*Validation* models. Add a new validation model and specify your
loader.io token (e.g., ``loaderio-28016b04fdb0ed4ea066ecec5a19c1ad``).

That's all you need to do. Your Django site should now respond to requests
against ``/<your loader.io token>`` (e.g., ``/loaderio-28016b04fdb0ed4ea066ecec5a19c1ad``).
