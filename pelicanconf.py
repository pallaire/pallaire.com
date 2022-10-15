AUTHOR = 'Patrick Allaire'
SITENAME = 'PALLAIRE'
SITEURL = 'https://pallaire.com'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('YouTube', 'https://www.youtube.com/channel/UCNqJR9etHn6xOyU505DiN_A'),
          ('Instagram', 'https://www.instagram.com/pallaire/'),)

DEFAULT_PAGINATION = 16

SUMMARY_MAX_LENGTH = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/grid_theme'
