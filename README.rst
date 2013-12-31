django-adminlang
============

Keep control of Django admin site's language.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-adminlang

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/philippeowagner/django-adminlang.git#egg=adminlang-master

TODO: Describe further installation steps (edit / remove the examples below):

Add ``adminlang`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'adminlang',
    )

Add the ``adminlang`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^adminlang/', include('adminlang.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load adminlang_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate adminlang


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-adminlang
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
