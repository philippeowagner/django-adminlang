django-adminlang
================

Keep control of Django admin site's language. 
-- 

The idea behind django-adminlang is to keep language consistent in the admin site. This allows to display the Django admin site in a predefined language (for example in English), even if the superuser was browsing (for example in German) through the website. This avoids to display a multilingual mix due to missing or broken translations of reusable apps and other third party components. This improves the usability and user experience.


Installation
------------

To get the latest stable release from PyPi

    TODO pip install django-adminlang

To get the latest commit from GitHub

    pip install -e git+git://github.com/philippeowagner/django-adminlang.git#egg=adminlang-master


Add ``adminlang`` to your ``INSTALLED_APPS``

    INSTALLED_APPS = (
        ...,
        'adminlang',
    )

