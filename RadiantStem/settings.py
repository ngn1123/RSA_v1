import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for RadiantStem project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oq-gd)t6dz9*b%_owi$o#d&r!2_&18#a_c7pyng!k_0+91c=3w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'radiantstem@gmail.com'
EMAIL_HOST_PASSWORD = 'Radiantjun_3'


# Application definition



ROOT_URLCONF = 'RadiantStem.urls'

WSGI_APPLICATION = 'RadiantStem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'RadiantStem', 'static'),
)
SITE_ID = 1

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)

PAYPAL_RECEIVER_EMAIL = "radiantstem@gmail.com"

PAYPAL_TEST = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': u'RadiantStemDemo',
        'HOST': u'localhost',
        'USER': u'postgres',
        'PASSWORD': u'postgres',
        'PORT': 5432
    }
}

MIGRATION_MODULES = {
    'cms': 'cms.migrations_django',
    'menus': 'menus.migrations_django',
    'djangocms_text_ckeditor': 'djangocms_text_ckeditor.migrations_django',
    'djangocms_column': 'djangocms_column.migrations_django',
    'djangocms_flash': 'djangocms_flash.migrations_django',
    'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    'djangocms_inherit': 'djangocms_inherit.migrations_django',
    'djangocms_style': 'djangocms_style.migrations_django',
    'djangocms_file': 'djangocms_file.migrations_django',
    'djangocms_link': 'djangocms_link.migrations_django',
    'djangocms_picture': 'djangocms_picture.migrations_django',
    'djangocms_teaser': 'djangocms_teaser.migrations_django',
    'djangocms_video': 'djangocms_video.migrations_django',
    'cmsplugin_cascade': 'cmsplugin_cascade.migrations',
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings',
    'zinnia.context_processors.version',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'RadiantStem', 'templates'),
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django_select2',
    'cmsplugin_cascade',
    'cms',
    'menus',
    'mptt',
    'filer',
    'easy_thumbnails',
    'sekizai',
    'django_comments',
    'tagging',
    'zinnia',
    #'cmsplugin_zinnia',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    # 'djangocms_inherit',
    # 'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    #'reversion',
    'RadiantStem',
    'rest_framework',
    'registration',
    'paypal.standard.ipn',
    'paypal_rsa',
)

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('page.html', 'Page'),
    ('feature.html', 'Page with Feature'),
    ('scroll.html', 'Page with Scroll'),
    ('leftMenu_page.html', 'Left Menu'),
    ('paypal_page.html', 'Page with Paypal')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
    'Main Content': {
        'plugins': ['BootstrapContainerPlugin'],
    },
}

CMSPLUGIN_CASCADE_PLUGINS = ('cmsplugin_cascade.link', 'cmsplugin_cascade.bootstrap3',)

# CMSPLUGIN_CASCADE_WITH_SHARABLES = {
#     'BootstrapImagePlugin': ('image-shapes', 'image-width-responsive', 'image-width-fixed', 'image-height', 'resize-options',),
#     'BootstrapPicturePlugin': ('image-shapes', 'responsive-heights', 'image-size', 'resize-options',),
#     'BootstrapButtonPlugin': ('link',),
#     'TextLinkPlugin': ('link', 'target',),
# }

# CMSPLUGIN_CASCADE_LEAF_PLUGINS = ('TextLinkPlugin',)

COLUMN_GLOSSARY = {
    'breakpoints': ['xs', 'sm', 'md', 'lg'],
    'container_max_widths': {'xs': 750, 'sm': 750, 'md': 970, 'lg': 1170},
    'fluid': False,
    'media_queries': {
        'xs': ['(max-width: 768px)'],
        'sm': ['(min-width: 768px)', '(max-width: 992px)'],
        'md': ['(min-width: 992px)', '(max-width: 1200px)'],
        'lg': ['(min-width: 1200px)'],
    },
}

CMS_PLACEHOLDER_CONF = {
    'Bootstrap Column': {
        'plugins': ['BootstrapRowPlugin', 'TextPlugin'],
        'parent_classes': {'BootstrapRowPlugin': []},
        'require_parent': False,
        'glossary': COLUMN_GLOSSARY,
    },
}

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'skin': 'moono',
    'toolbar': 'CMS',
}

FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS = True

FILER_DUMP_PAYLOAD = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    #'easy_thumbnails.processors.scale_and_crop',
    'easy_thumbnails.processors.filters',
)

THUMBNAIL_HIGH_RESOLUTION = False

THUMBNAIL_PRESERVE_EXTENSIONS = True

THUMBNAIL_OPTIMIZE_COMMAND = {
    'png': '/opt/local/bin/optipng {filename}',
    'gif': '/opt/local/bin/optipng {filename}',
    'jpeg': '/opt/local/bin/jpegoptim {filename}',
}
