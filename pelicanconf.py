#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Custom Jinja Filters
def create_groupby_key(list, attribute):
    for item in list:
        item.__key = getattr(item, attribute) if hasattr(item, attribute) else ''

    return list
 
JINJA_FILTERS = {
    'create_groupby_key': create_groupby_key,
}

# General
PATH = 'content'
AUTHOR = u'Barry Steyn'
SITENAME = u'Doctrina'
SITEURL = u'http://doctrina'

# URL
RELATIVE_URLS=False
DEFAULT_PAGINATION=False

#Category
USE_FOLDER_AS_CATEGORY=True
DEFAULT_CATEGORY=('misc')

# Locale
TIMEZONE = 'Canada/Pacific'
DEFAULT_LANG='en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Content
TYPOGRIFY=False
DEFAULT_DATE_FORMAT = ('%d  %b  %Y')
MARKUP = ('md', 'html')

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# SAAS Services
#GOOGLE_ANALYTICS = 'UA-33789117-1'
DISQUS_SHORTNAME = 'doctrinalocal'
#TWITTER_USERNAME = u'barrysteyn'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Plugins
PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = [
    'extract_toc',  # extracts [TOC] to variable that can be used in template
    'render_math'   # my render math plugin :)
]

#Render Math Plugin
MATH_JAX = {
    'linebreak_automatic':True
}

#Markdown Extensions
MD_EXTENSIONS = [
    'toc(title=Table Of Contents, permalink=True)',  # See https://pythonhosted.org/Markdown/extensions/toc.html for options
    'codehilite(css_class=highlight)'  # used for applying pygments.css to code
]

# Jinja2 Extensions
JINJA_EXTENSIONS = [
  'jinja2.ext.loopcontrols',
  'jinja2.ext.with_'
]

# Theme
THEME = 'doctrina-pelican_theme/Output'
