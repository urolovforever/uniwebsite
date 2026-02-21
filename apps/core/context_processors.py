from .models import SiteSettings


def site_context(request):
    """Inject site settings into every template."""
    try:
        settings = SiteSettings.load()
    except SiteSettings.DoesNotExist:
        settings = None

    return {
        'site_settings': settings,
    }
