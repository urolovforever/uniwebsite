from django import template
from django.utils.translation import get_language

register = template.Library()


@register.filter
def trans_field(obj, field_name):
    """Return the translated field value for the active language, falling back to English.

    Usage in templates:
        {{ article|trans_field:"title" }}
        {{ article|trans_field:"body"|safe }}
    """
    if obj is None:
        return ''
    lang = get_language()
    if lang and lang != 'en':
        translated = getattr(obj, f'{field_name}_{lang}', None)
        if translated:
            return translated
    return getattr(obj, field_name, '')
