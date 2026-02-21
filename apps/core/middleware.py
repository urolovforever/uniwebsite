from django.conf import settings


class ContentSecurityPolicyMiddleware:
    """Add Content-Security-Policy header to all responses."""

    def __init__(self, get_response):
        self.get_response = get_response
        self.csp = getattr(settings, 'CSP_POLICY', '')

    def __call__(self, request):
        response = self.get_response(request)
        if self.csp:
            response['Content-Security-Policy'] = self.csp
        return response
