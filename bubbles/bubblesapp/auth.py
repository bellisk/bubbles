from bubbles.bubblesapp.models import *
from django.http import HttpResponseForbidden

def profile(request):
    if not request.user.is_authenticated():
        return None
    if not request.user.profile:
        Profile(user=request.user).save()
    return request.user.profile
    

def logged_in(request):
    return request.user.is_authenticated()

def require_login(view_f):
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated():
            return view_f(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return inner


