from pelican import signals
from pelican.contents import Page

# General Configuration
# =====================
AUTHOR = 'Dr Saad Laouadi'
SITENAME = 'QCVersity'
SITEURL = "https://qcversity.github.io"

# Content Configuration
# =====================
PATH = "content"
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['static', 'images']


ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

PAGE_ORDER_BY = 'order'

# Define the explicit order of pages
PAGE_ORDER = ['Home', 'About', 'Contact']
DISPLAY_CATEGORIES_ON_MENU = True


CATEGORY_ORDER = {
    'Home': 1,
    'About': 2,
    'Contact': 3,
    'General': 4,
    'Julia': 5,
    'Programming': 6,
    'Technology': 7
}


TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Look and feel configurations
# ============================
# CSS_FILE = "main.css"

THEME_STATIC_DIR = 'theme/qcvtheme'
THEME = 'theme/qcvtheme'
# SITELOGO = 'images/ba-sa.svg'
# SITELOGO_SIZE = 64, 64



PYGMENTS_STYLE = 'emacs'

BANNER = "CC_BY"
BANNER_SUBTITLE = "The Data Science and Programming Hub for Aspiring People"
BOOTSTRAP_FLUID = True

# Creative Commons License Configuration
# ======================================
# Creative Commons License Configuration
CC_LICENSE = True
CC_LICENSE_NAME = "CC-BY-SA"
CC_LICENSE_DERIVATIVES = "ShareAlike"
CC_LICENSE_COMMERCIAL = "Yes"
CC_LICENSE_BR_AFTER_ICON = False
CC_LICENSE_ATTR_MARKUP = True
CC_LICENSE_ATTR_PROPS = {
    'lang': 'en',
    'title': 'Quant Coding Versity',
    'name': 'Dr Saad Laouadi',
    'url': 'http://www.mywebsite.com'
}

# The following variables can be dynamically set based on above settings
CC_LICENSE_TITLE = "Creative Commons Attribution-ShareAlike 4.0 International License"
CC_LICENSE_URI = "https://creativecommons.org/licenses/by-sa/4.0/"
CC_LICENSE_ICON = "//i.creativecommons.org/l/by-sa/4.0/80x15.png"

# PLUGIN_PATHS = ['path/to/your/plugins']

# PLUGINS = ['i18n_subsites']

# JINJA_ENVIRONMENT = {
#     'extensions': ['jinja2.ext.i18n'],
# }

# Variable to identify the home page
# IS_HOME_PAGE = True

# Content of the About Me section
# ===============================
ABOUT_ME = True
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
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/saadlaouadi"),
    ("Facebook", "https://www.facebook.com/drsaadlaouadi"),
    ("Instagram", "https://www.instagram.com/drsaadl"),
    ("GitHub", "https://github.com/DrSaadLa"),
    ("YouTube", "https://www.youtube.com/@QuantCodingSpace"),
    # ("Telegram", "https://t.me/yourusername"),
)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


def add_order_to_pages(generator):
    for page in generator.pages:
        # Default to 999 if Order is not specified
        order = page.metadata.get('Order', 999)
        setattr(page, 'order', int(order))


def register():
    signals.page_generator_finalized.connect(add_order_to_pages)


def sort_pages(pages):
    return sorted(pages, key=lambda page: page.metadata.get('order', 0))


TEMPLATE_CONTEXTS = {
    'sort_pages': sort_pages,
}


def generate_ordered_pages(generator):
    ordered_pages = sorted(generator.pages, key=lambda p: PAGE_ORDER.index(
        p.title) if p.title in PAGE_ORDER else 999)
    generator.context['ordered_pages'] = ordered_pages


def register():
    signals.page_generator_finalized.connect(generate_ordered_pages)


def sorted_categories(categories):
    return sorted(categories, key=lambda cat: CATEGORY_ORDER.get(cat[0], 999))


def add_to_context(generator):
    generator.context['sorted_categories'] = sorted_categories(
        generator.context.get('categories', []))


signals.generator_init.connect(add_to_context)
