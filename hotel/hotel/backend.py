from customauth.models import APIKey

def authenticate(request):
    # check if the user is authenticated by checking for an API key in the request headers
    api_key = request.headers.get('X-API-Key')
    if api_key:
        try:
            api_key_obj = APIKey.objects.get(key=api_key)
            print(api_key_obj)
            return True
        except APIKey.DoesNotExist:
            return False
    else:
        return False

