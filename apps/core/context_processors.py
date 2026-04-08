import re
from django.conf import settings as django_settings


def site_context(request):
    """Inject common context into every template."""
    # Strip language prefix from path for language switcher
    lang_codes = [code for code, _ in django_settings.LANGUAGES]
    lang_prefix_re = re.compile(r'^/(' + '|'.join(lang_codes) + ')/')
    path_no_lang = lang_prefix_re.sub('/', request.path)

    return {
        'path_no_lang': path_no_lang,
    }
