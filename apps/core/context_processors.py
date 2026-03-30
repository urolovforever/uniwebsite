import re
from django.conf import settings as django_settings
from .models import SiteSettings


def site_context(request):
    """Inject site settings into every template."""
    try:
        site_settings = SiteSettings.load()
    except SiteSettings.DoesNotExist:
        site_settings = None

    # Strip language prefix from path for language switcher
    lang_codes = [code for code, _ in django_settings.LANGUAGES]
    lang_prefix_re = re.compile(r'^/(' + '|'.join(lang_codes) + ')/')
    path_no_lang = lang_prefix_re.sub('/', request.path)

    return {
        'site_settings': site_settings,
        'path_no_lang': path_no_lang,
    }
