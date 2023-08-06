==========================
django-country-dialcode-sb
==========================

Major code is taken from http://github.com/Star2Billing/django-country-dialcode

This Django application provides Dial Code and Country data to reuse in a django application.


Installation
============

Install Django-Country-Dialcode::

    python setup.py install


Settings
========

in your settings.py file::

    INSTALLED_APPS = INSTALLED_APPS + ('country_dialcode',)


Usage
=====

In your models add the following ::

    dialcode = models.ForeignKey(Prefix, verbose_name=_("Destination"), null=True,
                               blank=True, help_text=_("Select Prefix"))


