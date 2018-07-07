#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Stuart M. Davis'
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

# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/stuartmdavis', 'twitter'),
          ('linkedin', 'http://www.linkedin.com/in/stuartmdavis/', 'linkedin'),
          ('reddit', 'https://www.reddit.com/user/smdavis42', 'reddit'),
          ('instagram', 'https://www.instagram.com/stuartmdavis/', 'instagram'),
          ('pinterest', 'https://www.pinterest.com/stuartmdavis/', 'pinterest'),
          ('quora', 'https://www.quora.com/profile/Stuart-Davis-2', 'quora'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# These are my added items
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
GITHUB_URL = 'https://github.com/brokenlyre/'
TWITTER_USERNAME = 'stuartmdavis'
STATIC_PATHS = [
	'extra/CNAME','media','extra/README.MD','extra/favicon.ico'
	]
EXTRA_PATH_METADATA = {
    'extra/README.MD': {'path': 'README.md'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'}
}

# Theme specifics
THEME = 'pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
MENUITEMS = (
    ('Pilosophies', '/pages/stuart-m-davis-philosophies.html'),
    ('Blog', '/category/blog.html'),
    ('CV', '/pages/stuart-m-davis-resume.html')
    )   
PLUGIN_PATHS = ['C:\\Users\\Stuart\\projects\\pelican-plugins\\pelican-plugins']
PLUGINS = ['i18n_subsites', 'tag_cloud', 'summary']
BOOTSTRAP_NAVBAR_INVERSE = True
FAVICON = './favicon.ico'
ABOUT_ME = 'Obstacle Crusher and Creativity Beckoner. Regardless of the position I am in, I develop fiercely honest relationships that advance personal growth, critical thinking and boldly simply execution.'
AVATAR = '/media/SMD_Self.jpg'
DISPLAY_TAGS_ON_SIDEBAR = 'True'
TAGS_URL = 'tags.html'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
DISPLAY_ARCHIVE_ON_SIDEBAR = True