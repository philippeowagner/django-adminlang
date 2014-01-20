from django.conf import settings
from django.utils import translation


class AdminLangMiddleware:
    
    def process_request(self, request):
        matchPatterns = getattr(settings, 'ADMIN_LANGUAGE_EXCLUDE_PATH_PATTERNS', [])
        for pattern in matchPatterns:
            if request.path.startswith(pattern):
                return None
        if request.path.startswith('/admin'):
            request.LANG = getattr(settings, 'ADMIN_LANGUAGE_CODE', settings.LANGUAGE_CODE)
            translation.activate(request.LANG)
            request.LANGUAGE_CODE = request.LANG
    
    def process_response(self, request, response):
        ''' cleanup '''
        translation.deactivate()
        return response