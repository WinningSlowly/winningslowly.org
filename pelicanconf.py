#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Krycho', 'Stephen Carradini'
SITENAME = 'Winning Slowly'
SITE_DESCRIPTION = 'Culture, art, religion, and ethics—from the long view.'
SITEURL = ''
LOGO = '/static/images/winning-slowly_circle.png'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = "design"

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_RSS = None
CUSTOM_FEED_URL = 'feed.xml'

# Social widget
IDENTITY = {'Site': {'App.net': 'https://app.net/winningslowly',
                     'App.net Broadcast': 'https://broadcast.app.net/40022/winning-slowly-episodes/',
                     'Twitter': 'https://twitter.com/winningslowly',
                     'Google+': 'https://plus.google.com/+WinningslowlyOrgCast',},
            'Chris': {'App.net': 'https://app.net/chriskrycho',
                      'Twitter': 'https://twitter.com/chriskrycho',
                      'Homepage': 'http://chriskrycho.com',},
            'Stephen': {'Twitter': 'https://twitter.com/scarradini',
                        'Homepage': 'http://stephencarradini.com',},}

DEFAULT_PAGINATION = 10

# Category settings
USE_FOLDER_AS_CATEGORY = True  # note: this is the default
DEFAULT_CATEGORY = 'episodes'

# Disable unused elements
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
CATEGORY_SAVE_AS = False
TAGS_SAVE_AS = False

# Metadata
DEFAULT_METADATA = (('Author', ('Chris Krycho', 'Stephen Carradini')),)

# Output
OUTPUT_SOURCES = True
OUTPUT_SOURCES_EXTENSION = ".txt"

# Markdown settings
MD_EXTENSIONS = ['extra', 'toc', 'headerid']
TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Path configuration
STATIC_PATHS = ['extra/CNAME',
                'extra/favicon.ico',
                'extra/favicon.png',]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'},
                       'extra/favicon.png': {'path': 'favicon.png'},}

# Custom 404 page
TEMPLATE_PAGES = {'extra/404.html': '404.html'}

# Static configuration
THEME_STATIC_DIR = 'assets'
CSS_FILE = 'min.css'
