from django.shortcuts import redirect
from django.conf import settings

def token_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.session.get('token'):
            return redirect()
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func