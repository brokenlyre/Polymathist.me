#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Stuart'
SITENAME = 'Stuart M. Davis - Polymath'
SITEURL = 'http://www.polymathist.me'

PATH = 'content'

TIMEZONE = 'America/Detroit'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# These are my added items
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (('Pilosophies', '/pages/stuart-m-davis-philosophies.html'),
    ('Blog', '/category/blog.html'),
    )
GITHUB_URL = 'https://github.com/brokenlyre/'
TWITTER_USERNAME = 'stuartmdavis'
STATIC_PATHS = [
	'CNAME','media','favicon.ico'
	]
THEME = 'pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['C:\\Users\\Stuart\\projects\\pelican-plugins\\pelican-plugins']
PLUGINS = ['i18n_subsites']