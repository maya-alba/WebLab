#sfrom django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    return render_to_response('index.html',
        {},
        context_instance=RequestContext(request)
    )
def account(request):
    return render_to_response('account.html',
        {},
        context_instance=RequestContext(request)
    )
def categories(request):
    return render_to_response('categories.html',
        {},
        context_instance=RequestContext(request)
    )
def checkout(request):
    return render_to_response('checkout.html',
        {},
        context_instance=RequestContext(request)
    )
def editservice(request):
    return render_to_response('editservice.html',
        {},
        context_instance=RequestContext(request)
    )
def login(request):
    return render_to_response('login.html',
        {},
        context_instance=RequestContext(request)
    )
def myinfoaccount(request):
    return render_to_response('myinfoaccount.html',
        {},
        context_instance=RequestContext(request)
    )
def myservices(request):
    return render_to_response('myservices.html',
        {},
        context_instance=RequestContext(request)
    )
def offerservice(request):
    return render_to_response('offerservice.html',
        {},
        context_instance=RequestContext(request)
    )
def register(request):
    return render_to_response('register.html',
        {},
        context_instance=RequestContext(request)
    )
def saleshistory(request):
    return render_to_response('saleshistory.html',
        {},
        context_instance=RequestContext(request)
    )
def serviceoverview(request):
    return render_to_response('serviceoverview.html',
        {},
        context_instance=RequestContext(request)
    )
def servicelist(request):
    return render_to_response('servicelist.html',
        {},
        context_instance=RequestContext(request)
    )
def shophistory(request):
    return render_to_response('shophistory.html',
        {},
        context_instance=RequestContext(request)
    )
