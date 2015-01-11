#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Custom Jinja Filters
def get_attribute_index(list, attribute, index):
    seen = set()
    new_list = [getattr(list_item, attribute)[index]
        for list_item in list if not (getattr(list_item, attribute)[index]
        in seen or seen.add(getattr(list_item, attribute)[index]))]
   
    return new_list
 
 
def sort_attribute_index(list, attribute, index):
    return sorted(list, key = lambda x: getattr(x, attribute)[index])

def create_groupby_key(list, attribute, index):
    for item in list:
        item.__key = getattr(item, attribute)[index]

    return list
 
JINJA_FILTERS = {
    'get_attribute_index': get_attribute_index,
    'sort_attribute_index': sort_attribute_index
}

AUTHOR = u'Barry Steyn'
SITENAME = u'Doctrina'
SITEURL = u'http://doctrina'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Plugins
PLUGIN_PATHS = ['../../Programming/GitHub/pelican-plugins/']
PLUGINS = [
    'extract_toc',  # extracts [TOC] to variable that can be used in template
    'render_math'   # my render math plugin :)
]

#Markdown Extensions
MD_EXTENSIONS = [
    'toc(title=Table Of Contents, permalink=True)'  # See https://pythonhosted.org/Markdown/extensions/toc.html for options
]

# Jinja2 Extensions
JINJA_EXTENSIONS = ['jinja2.ext.loopcontrols']

# Theme
THEME = 'doctrina-pelican_theme/Output'
