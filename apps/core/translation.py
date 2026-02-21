from django.utils.translation import get_language


class TranslatedMixin:
    """Mixin that resolves the correct translated field by active language.

    Usage on a model instance:
        article.t('title')   ->  article.title_uz  (if language is 'uz' and value exists)
                              ->  article.title     (fallback to English)
    """

    def t(self, field_name):
        lang = get_language()
        if lang and lang != 'en':
            translated = getattr(self, f'{field_name}_{lang}', None)
            if translated:
                return translated
        return getattr(self, field_name)
