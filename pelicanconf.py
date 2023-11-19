# General Configuration
# =====================
AUTHOR = 'Dr Saad Laouadi'
SITENAME = 'QCVersity'
SITEURL = "https://qcversity.github.io/"

# Content Configuration
# =====================
PATH = "content"
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']

ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Look and feel configurations
# ============================
# CSS_FILE = "main.css"

THEME_STATIC_DIR = 'theme/qcvtheme'
THEME = 'theme/qcvtheme'

PYGMENTS_STYLE = 'emacs'

# PLUGIN_PATHS = ['path/to/your/plugins']

PLUGINS = ['i18n_subsites']

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Metadata configuration
# ======================
# DEFAULT_METADATA = {
#    'status': 'draft',
# }


# Code Style Configuration
# ========================

# PYGMENTS_RST_OPTIONS = {
#     'linenos': 'table',
#     'style': 'manni',
#     # 'noclasses': True,
#     'pygments_style': 'vim'
# }


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/saadlaouadi"),
    ("Facebook", "https://www.facebook.com/drsaadlaouadi"),
    ("Instagram", "https://www.instagram.com/drsaadl"),
    ("GitHub", "https://github.com/DrSaadLa"),
    ("YouTube", "https://www.youtube.com/channel/QuantCodingSpace"),
    ("Telegram", "https://t.me/yourusername"),
)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
