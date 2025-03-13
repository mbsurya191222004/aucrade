from django.utils.deprecation import MiddlewareMixin

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'jwt' in request.COOKIES:
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {request.COOKIES["jwt"]}'