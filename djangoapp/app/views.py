# coding: utf-8
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from models import *
from forms import *

def home(request):
    return render_to_response('index.html',
        {"user": request.user},
        context_instance=RequestContext(request)
    )

def about(request):
    return render_to_response('about.html',
        {},
        context_instance=RequestContext(request)
    )

@login_required(login_url='/login/')
def account(request):
    return render_to_response('account.html',
        {"user": request.user},
        context_instance=RequestContext(request)
    )

def categories(request):
    return render_to_response('categories.html',
        {
            "user": request.user,
            "service_types_1": SERVICE_TYPES[:3],
            "service_types_2": SERVICE_TYPES[3:],
        },
        context_instance=RequestContext(request)
    )

@login_required(login_url='/login/')
def checkout(request):
    return render_to_response('checkout.html',
        {"user": request.user},
        context_instance=RequestContext(request)
    )

@login_required(login_url='/login/')
def editservice(request):
    return render_to_response('editservice.html',
        {"user": request.user},
        context_instance=RequestContext(request)
    )

@login_required(login_url='/login/')
def myinfoaccount(request):
    if request.POST:
        edit_form = EditProfile(request.POST)
        if edit_form.is_valid():
            user_name = edit_form.cleaned_data['user_name']
            user_last_name = edit_form.cleaned_data['user_last_name']
            user_password = edit_form.cleaned_data['user_password']
            user = User.objects.get(id = request.user.id)
            if user_name:
                user.first_name = user_name
            if user_last_name:
                user.last_name = user_last_name
            if user_password:
                user.set_password(user_password)
            user.save()
            message = "Modificación exitosa"
            return render_to_response('myinfoaccount.html',
                {
                    "return_message": message,
                    "user": request.user,
                    "edit_form": edit_form
                },
                context_instance=RequestContext(request)
            )
    else:
        edit_form = EditProfile()
    return render_to_response('myinfoaccount.html',
        {
            "user": request.user,
            "edit_form":  edit_form
        },
        context_instance=RequestContext(request)
    )

@login_required(login_url='/login/')
def myservices(request):
    return render_to_response('myservices.html',
        {"user": request.user},
        context_instance=RequestContext(request)
    )

@login_required(login_url='/login/')
def offerservice(request):
    if request.POST:
        add_service_form = AddServiceForm(request.POST)
        if add_service_form.is_valid():
            service_title = add_service_form.cleaned_data['service_title']
            service_type = add_service_form.cleaned_data['service_type']
            service_is_company = add_service_form.cleaned_data['service_is_company']
            service_company_name = add_service_form.cleaned_data['service_company_name']
            service_account = add_service_form.cleaned_data['service_account']
            service_price = add_service_form.cleaned_data['service_price']
            service_price_delimiter = add_service_form.cleaned_data['service_price_delimiter']
            service_state = add_service_form.cleaned_data['service_state']
            service_city = add_service_form.cleaned_data['service_city']
            service_image = add_service_form.cleaned_data['service_image']
            service_brief_desc =  add_service_form.cleaned_data['service_brief_desc']
            service_description = add_service_form.cleaned_data['service_description']
            service_email = add_service_form.cleaned_data['service_email']
            service_telephone = add_service_form.cleaned_data['service_telephone']

            user_email = request.user.username

            service = OfferedService.objects.create(user_email=request.user,
                title = service_title,
                service_type = service_type,
                company = service_is_company,
                company_name = service_company_name,
                account = service_account,
                price = service_price,
                price_delimiter = service_price_delimiter,
                state = service_state,
                city =service_city,
                service_image = service_image,
                brief_description = service_brief_desc,
                descripton = service_description,
                service_email = service_email,
                telephone = service_telephone
            )
            service.save()

            message = "<p>Gracias por crear servicio.</p>"
            return render_to_response('offerservice.html',
                {"message_return": message},
                context_instance=RequestContext(request)
            )
    else:
        message = "<p>error :(</p>"
        add_service_form = AddServiceForm()
    return render_to_response('offerservice.html',
        {"user": request.user,
        "add_service_form": add_service_form},
        context_instance=RequestContext(request)
    )

def profile(request):
    return HttpResponseRedirect('/myinfoaccount')

def register(request):
    if request.POST:
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = register_form.cleaned_data['user_name']
            user_lname = register_form.cleaned_data['user_lname']
            email = register_form.cleaned_data['email']
            user_password = register_form.cleaned_data['user_password']
            user, created = User.objects.get_or_create(username = email)
            if not created:
                message = u"<p>Lo sentimos, pero el usuario " + email + u" ya se encuentra registrado.<br/>"
                message += u"Si has olvidado tu contraseña, da click <a href='/reset_password/"+ email + u"'>aquí</a>"
                message += u" para reestablecerla.</p>"
                return render_to_response('register.html',
                    {"message_return": message},
                    context_instance=RequestContext(request)
                )
            user.first_name = user_name
            user.last_name = user_lname
            user.email = email
            user.is_active = True
            user.set_password(user_password)
            user.save()
            message = "<p>Gracias por registrarte.</p>"
            return render_to_response('register.html',
                {"message_return": message},
                context_instance=RequestContext(request)
            )
    else:
        register_form = RegisterForm()
    return render_to_response('register.html',
        {"register_form": register_form},
        context_instance=RequestContext(request)
    )

@login_required(login_url='/login/')
def saleshistory(request):
    return render_to_response('saleshistory.html',
        {"user": request.user},
        context_instance=RequestContext(request)
    )

def serviceoverview(request, serv_id):
    service = OfferedService.objects.get(seviceID = serv_id)
    return render_to_response('serviceoverview.html',
        {"service" : service},
        context_instance=RequestContext(request)
    )

def servicelist(request, service):
    services = OfferedService.objects.filter(service_type = service).order_by("-rating")
    return render_to_response('servicelist.html',
        {
            "services" : services,
            "service_type" : service,
        },
        context_instance=RequestContext(request)
    )

@login_required(login_url='/login/')
def shophistory(request):
    return render_to_response('shophistory.html',
        {"user": request.user},
        context_instance=RequestContext(request)
    )
