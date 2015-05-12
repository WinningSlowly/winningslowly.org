#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Krycho and Stephen Carradini'
SITENAME = 'Winning Slowly'
SITE_DESCRIPTION = 'Culture, technology, religion, ethics, and art—from the long view.'
SITEURL = ''
LOGO = 'static/images/winning-slowly_circle.png'
PODCAST_LOGO = 'static/images/winning-slowly_podcast_small.png'

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
IDENTITY = {'Site': {'RSS': FEED_DOMAIN + '/' + CUSTOM_FEED_URL,
                     'iTunes': 'https://itunes.apple.com/us/podcast/winning-slowly/id807603957?mt=2',
                     'Facebook': 'https://www.facebook.com/winningslowlypodcast',
                     'App.net': 'https://app.net/winningslowly',
                     'App.net Broadcast': 'https://broadcast.app.net/40022/winning-slowly-episodes/',
                     'Twitter': 'https://twitter.com/winningslowly',},
            'Chris': {'App.net': 'https://app.net/chriskrycho',
                      'GitHub': 'https://github.com/chriskrycho',
                      'Twitter': 'https://twitter.com/chriskrycho',
                      'Homepage': 'http://chriskrycho.com',},
            'Stephen': {'Twitter': 'https://twitter.com/scarradini',
                        'Homepage': 'http://stephencarradini.com',},}

PODTRAC_REDIRECT = 'http://www.podtrac.com/pts/redirect'
PODTRAC_M4A = PODTRAC_REDIRECT + '.m4a'
PODTRAC_MP3 = PODTRAC_REDIRECT + '.mp3'

DEFAULT_PAGINATION = 10

# URLs
SLUGIFY_SOURCE='basename'
ARTICLE_URL = '{number}/'
ARTICLE_SAVE_AS = '{number}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Category settings
USE_FOLDER_AS_CATEGORY = True  # note: this is the default
DEFAULT_CATEGORY = 'episodes'
DIRECT_TEMPLATES = ('index', 'tags', 'archives')

# Disable unused elements
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
CATEGORY_SAVE_AS = False
TAGS_SAVE_AS = False

# Output
OUTPUT_SOURCES = True
OUTPUT_SOURCES_EXTENSION = ".txt"

# Markdown settings
MD_EXTENSIONS = ['extra', 'markdown.extensions.smarty']

DEFAULT_DATE_FORMAT = "%B %d, %Y"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Path configuration
STATIC_PATHS = ['images',
                'extra/CNAME',
                'extra/favicon.ico',
                'extra/favicon.png',
                'extra/feed.xml',
                'extra/test_feed.xml',
                'extra/Winning-Slowly_podcast.png']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'},
                       'extra/favicon.png': {'path': 'favicon.png'},
                       'extra/feed.xml': {'path': CUSTOM_FEED_URL},
                       'extra/test_feed.xml': {'path': 'test_feed.xml'},
                       'extra/Winning-Slowly_podcast.png': {'path': 'podcast.png'}}

# Custom 404 page
# TEMPLATE_PAGES = {'extra/404.html': '404.html'}

# Static configuration
THEME_STATIC_DIR = 'assets'
CSS_FILE = 'min.css'
