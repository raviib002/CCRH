"""
Django settings for ccrh project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*ubmb)x@*m1pv15=6^l%js)j+dh0x_xug&5i9feytjxmwsz=f&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['ccrh.azurewebsites.net']
SITE_ID = 1
ADMIN_EMAIL = 'smtp@baryonssoftsolutions.com'
# Application definition

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'cms',
    'menus',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_link',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_style',  
    'sekizai',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_video',
    'cms_plugins',
    'debug_toolbar',
    'master',
    'utils',
    'user_profile',
    'import_export',
    'admin_reorder',
    'djangocms_forms',
    'meta', #DJango CMS Meta tags plugin
    'djangocms_page_meta', #DJango CMS Meta tags plugin
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'audit_log.middleware.UserLoggingMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'ccrh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'ccrh.wsgi.application'
#Media Configurations
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'ccrhmysql',
        'USER': 'ccrhmysql@ccrhmysql',
        'PASSWORD': 'Baryons@12345',
        'HOST': 'ccrhmysql.mariadb.database.azure.com',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'user_profile.password_validator.NumberValidator', 
    },
    {
        'NAME': 'user_profile.password_validator.UppercaseValidator', 
    },
    {
        'NAME': 'user_profile.password_validator.LowercaseValidator', 
    },
    {
        'NAME': 'user_profile.password_validator.SymbolValidator', 
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False

LANGUAGES = (
    ('en', _('English')),
#     ('hi', _('Hindi')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)

LOGIN_ERROR_URL    = '/'
LOGIN_URL    = 'user_profile:login'
LOGOUT_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'user_profile.email_auth.EmailAuthBackend',
)


'''CMS Settings Start Here'''
CMS_TEMPLATES = (
    ('cms/home.html', 'Home'),
    ('cms/contact_us.html', 'Contact Us'),
    ('cms/faq.html', 'FAQ'),
    ('cms/rti.html', 'RTI'),
    ('cms/submit.html', 'Submit'),
    ('cms/submit-a-manuscript.html', 'Submit A Manuscript'),
    ('cms/e-tutorials.html', 'E-Tutorials'),
    
    ('cms/about_us/about_us.html', 'About Us'),
    ('cms/about_us/aims-and-scope.html', 'Aims And Scope'),
    ('cms/about_us/authors-incentives.html', 'Authors Incentives'),
    ('cms/about_us/editorial-reviewers-board.html', 'Editorial Reviewers Board'),
    ('cms/about_us/why-publish-hccr.html', 'Why Publish Hccr'),
    
    ('cms/editorial_policies/appeals-and-complaints-policy.html', 'Appeals And Complaints Policy'),
    ('cms/editorial_policies/commercial-use-and-reprints.html', 'Commercial Use And Reprints'),
    ('cms/editorial_policies/copyright-and-licenses.html', 'Copyright And Licenses'),
    ('cms/editorial_policies/data-deposition-and-data-sharing.html', 'Data Deposition And Data Sharing'),
    ('cms/editorial_policies/editorial-policies.html', 'Editorial Policies'),
    ('cms/editorial_policies/peer-review.html', 'Peer Review'),
    ('cms/editorial_policies/plagiarism-detection.html', 'Plagiarism Detection'),
    ('cms/editorial_policies/publication-ethics.html', 'Publication Ethics'),
    ('cms/editorial_policies/reporting-guidelines.html', 'Reporting Guidelines'),
    ('cms/editorial_policies/scientific-misconduct.html', 'Scientific Misconduct'),
    ('cms/editorial_policies/text-and-data-mining.html', 'Text And Data Mining'),
    
    ('cms/submission_guidelines/clinical-trial-registration.html', 'Clinical Trial Registration'),
    ('cms/submission_guidelines/conflict-interest-policies.html', 'Conflict Interest Policies'),
    ('cms/submission_guidelines/copyrights-authors-readers-and-publisher.html', 'Copyrights Authors Readers And Publisher'),
    ('cms/submission_guidelines/ethics.html', 'Ethics'),
    ('cms/submission_guidelines/guide-submission-status.html', 'Guide Submission Status'),
    ('cms/submission_guidelines/manuscript-organization.html', 'Manuscript Organization'),
    ('cms/submission_guidelines/manuscript-preparation.html', 'Manuscript Preparation'),
    ('cms/submission_guidelines/manuscript-templates.html', 'Manuscript Templates'),
    ('cms/submission_guidelines/pre-submissions.html', 'Pre Submissions'),
    ('cms/submission_guidelines/privacy-policy.html', 'Privacy Policy'),
    ('cms/submission_guidelines/submission-guidelines.html', 'Submission Guidelines'),
    ('cms/submission_guidelines/submission-manuscripts.html', 'Submission Manuscripts'),
    ('cms/submission_guidelines/terms-publication.html', 'Terms Publication'),
    ('cms/submission_guidelines/tnc.html', 'T & C'),
)

CMS_PERMISSION = True
CMS_PLACEHOLDER_CONF = {}
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

CMS_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'name': _('English'),
            'fallbacks': ['hi',],
            'public': True,
            'hide_untranslated': True,
            'redirect_on_fallback': False,
        },
#         {
#             'code': 'hi',
#             'name': _('Hindi'),
#             'fallbacks': ['en',],
#             'public': True,
#         },
    ],
    }
DJANGOCMS_FORMS_PLUGIN_NAME = _('Contact Us Form')
DJANGOCMS_FORMS_USE_HTML5_REQUIRED = False
DJANGOCMS_FORMS_WIDGET_CSS_CLASSES = {'__all__': ('form-control', ) }

DJANGOCMS_STYLE_TAGS = ['div', 'article', 'section', 'header', 'footer',
                       'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span',
                       'ul', 'ol', 'li', 'i', 'a']
META_SITE_PROTOCOL = 'http'
META_USE_SITES = True

'''CMS Settings End Here'''

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL = True
EMAIL_HOST = 'sg3plcpnl0228.prod.sin3.secureserver.net'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'smtp@baryonssoftsolutions.com'
EMAIL_HOST_PASSWORD = 'Baryons@123456'
DEFAULT_FROM_EMAIL = 'smtp@baryonssoftsolutions.com'
SEND_MAIL_ALL_PLACE = True

'''Email setting Ends'''

'''Case History API Endpoint'''
CASE_HISTORY_API = {
    'DOMAIN' : 'http://ccrhch.azurewebsites.net/en',
    'URL' : '/user/'
    }
CASE_HISTORY_LOGIN_URL = 'http://ccrhch.azurewebsites.net/en/user/login/'
CASE_HISTORY_REGISTRATION_URL = 'http://ccrhch.azurewebsites.net/en/user/registration/'

# Azure Static files rendering from the Azre Storage Blob
DEFAULT_FILE_STORAGE = 'ccrh.custom_azure.AzureMediaStorage'
STATICFILES_STORAGE = 'ccrh.custom_azure.AzureStaticStorage'

STATIC_LOCATION = "static"
MEDIA_LOCATION = "media"

AZURE_ACCOUNT_NAME = "ccrhhot"
AZURE_CUSTOM_DOMAIN = f'ccrhhot.blob.core.windows.net'
STATIC_URL = f'https://ccrhhot.blob.core.windows.net/ccrhstatic/'
MEDIA_URL = f'https://ccrhhot.blob.core.windows.net/ccrhmedia/'
