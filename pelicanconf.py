#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dinara S.'
SITENAME = u'About science, math and programming'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/oftomorrow'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
GITHUB_URL = 'http://github.com/oftomorrow/'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins',]
PLUGINS = ['ipynb.markup']
