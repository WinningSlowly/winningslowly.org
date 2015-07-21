#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from copy import copy

# Setup path to enable local helpers.
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))


# Site configuration
AUTHOR = 'Chris Krycho and Stephen Carradini'
SITENAME = 'Winning Slowly'
SITE_DESCRIPTION = 'Culture, technology, religion, ethics, and art—from the long view.'
SITEURL = ''
LOGO = 'static/images/winning-slowly_circle.png'
PODCAST_LOGO = 'static/images/winning-slowly_podcast_small.png'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = "design"

# Show configuration
CURRENT_SEASON = '3'

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
                     'Patreon': 'https://www.patreon.com/winningslowly',
                     'Square': 'https://cash.me/$winningslowly',
                     'App.net': 'https://app.net/winningslowly',
                     'Twitter': 'https://twitter.com/winningslowly'},
            'Chris': {'App.net': 'https://app.net/chriskrycho',
                      'GitHub': 'https://github.com/chriskrycho',
                      'Twitter': 'https://twitter.com/chriskrycho',
                      'Homepage': 'http://chriskrycho.com'},
            'Stephen': {'Twitter': 'https://twitter.com/scarradini',
                        'Homepage': 'http://stephencarradini.com'}}

CDN = 'cdn.winningslowly.org'
M4A = '.m4a'
MP3 = '.mp3'
PODTRAC_REDIRECT = 'http://www.podtrac.com/pts/redirect'
PODTRAC_M4A = PODTRAC_REDIRECT + M4A
PODTRAC_MP3 = PODTRAC_REDIRECT + MP3

DEFAULT_PAGINATION = False

# URLs
SLUGIFY_SOURCE = 'basename'
ARTICLE_URL = '{category}.{number}/'
ARTICLE_SAVE_AS = '{category}.{number}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
CATEGORY_URL = 'season-{slug}.html'
CATEGORY_SAVE_AS = 'season-{slug}.html'

# Category settings
USE_FOLDER_AS_CATEGORY = False  # note: this is the default
DEFAULT_CATEGORY = 'bonus'
DIRECT_TEMPLATES = ['index']

# Disable unused elements
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
TAGS_SAVE_AS = ''

# Output
OUTPUT_SOURCES = False
DEFAULT_DATE_FORMAT = "%B %d, %Y"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Path configuration
here = Path(__file__).parent
root = 'root'
root_path = here / 'show-notes' / 'root'
STATIC_PATHS = ['images', '2014', '2015', 'extra', root]
basic_path_metadata = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'},
                       'extra/favicon.png': {'path': 'favicon.png'},
                       'extra/feed.xml': {'path': CUSTOM_FEED_URL},
                       'extra/test_feed.xml': {'path': 'test_feed.xml'},
                       'extra/Winning-Slowly_podcast.png': {'path':
                                                            'podcast.png'},
                       'extra/humans.txt': {'path': 'humans.txt'}}

import helpers
show_notes = here / 'show-notes'
items = show_notes.glob('season-*/*.md')
root_metadata = helpers.root_redirects(items, root_path)

EXTRA_PATH_METADATA = basic_path_metadata.copy()
EXTRA_PATH_METADATA.update(root_metadata)

ARTICLE_EXCLUDES = ['2014', '2015', 'root']
PAGE_EXCLUDES = ['2014', '2015', 'root']

# Static configuration
THEME_STATIC_DIR = 'assets'
CSS_FILE = 'min.css'

READERS = {'html': None}

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['pandoc_reader']
PANDOC_ARGS = ['--smart']
PANDOC_EXTENSIONS = ['-citations']
