#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Krycho', 'Stephen Carradini'
SITENAME = 'Winning Slowly'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social widget
IDENTITY = {'Site': {'App.net': 'https://app.net/winningslowly',
                     'Twitter': 'https://twitter.com/winningslowly',},
            'Chris': {'App.net': 'https://app.net/chriskrycho',
                      'Twitter': 'https://twitter.com/chriskrycho',},
            'Stephen': {'Twitter': 'https://twitter.com/scarradini',},}

DEFAULT_PAGINATION = 10

# Category settings
USE_FOLDER_AS_CATEGORY = True  # note: this is the default
DEFAULT_CATEGORY = 'episodes'

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
STATIC_PATHS = ['extra/CNAME',  # Include the CNAME file
               ]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},  # Copy CNAME file to /output
                      }