from django.conf import settings
from django.core.cache import cache
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.middleware import AuthenticationMiddleware


class SamamMiddleware(AuthenticationMiddleware):

    def process_request(self, request):
        super().process_request(request)
        if request.user.is_authenticated:
            org = cache.get(settings.SAMAM_ORG_CACHE_KEY.format(request.user.username))
            if org:
                request.user.org = org
            else:
                request.user.org = None

        # Call the next middleware or view
        response = self.get_response(request)

        return response
