from django.shortcuts import redirect
from django.conf import settings
import requests
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def token_required(view_func):
    @csrf_exempt
    def _wrapped_view_func(request, *args, **kwargs):
        hallado = "user_token" in request.session
        print(hallado)
        if not hallado:
            return redirect()
        else:
            response = requests.get("http://35.190.51.156:8082/user/is_authenticated", headers=request.session["user_token"])
            print(response.text)
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func