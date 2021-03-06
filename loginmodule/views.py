from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf


def login(request):
    """

    :type request: object
    """
    c = {}
    c.update(csrf(request))
    return render_to_response("login.html", c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username,

                             password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loginmodule/loggedin/')
    else:
        return


HttpResponseRedirect('/loginmodule/invalidlogin/')


def loggedin(request):
    """

    :type request: object
    """
    return render_to_response('loggedin.html', {"full_name": request.user.username})


def invalidlogin(request):
    return render_to_response('invalidlogin.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')