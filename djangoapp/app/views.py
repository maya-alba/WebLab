# coding: utf-8
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Count, Avg
from django.views.decorators.cache import never_cache
from models import *
from forms import *

def home(request):
    top_services = PurchasedService.objects.values("seller_email").annotate(Count("seller_email")).order_by("-seller_email__count")
    top_info=[]
    if len(top_services)<4:
        for top in range(0,len(top_services)):
            top_info.append(OfferedService.objects.get(serviceID = top_services[top]['seller_email']))
    else:
        for top in range(0,4):
            top_info.append(OfferedService.objects.get(serviceID = top_services[top]['seller_email']))
    return render_to_response('index.html',
        {"user" : request.user,
        "top_services" : top_services,
        "top_info" : top_info},
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

def add_to_cart(request):
    if request.POST:
        service_id = request.POST['service_id']
        try:
            request.session["guru_cart"]
            try:
                request.session["guru_cart"][service_id] += 1
            except:
                request.session["guru_cart"][service_id] = 1
        except:
            request.session["guru_cart"] = {service_id : 1}
    request.session.modified = True
    return HttpResponse("Done")

def categories(request):
    return render_to_response('categories.html',
        {
            "user": request.user,
            "service_types_1": SERVICE_TYPES[:3],
            "service_types_2": SERVICE_TYPES[3:],
        },
        context_instance=RequestContext(request)
    )

def buy(request):
    if request.POST:
        services = dict(request.POST)['services[]']
        quantities = dict(request.POST)['quantities[]']
        for c, s in enumerate(services):
            os = OfferedService.objects.get(serviceID = int(s))
            ps = PurchasedService.objects.create(
                client_email = request.user,
                seller_email =  os,
                quantity = int(quantities[c]),
                total = float(os.price)*int(quantities[c])
            )
            ps.save()
    request.session.modified = True
    return HttpResponse("Done")

@login_required(login_url='/login/')
def checkout(request):
    services = []
    total = 0.0
    try:
        cart = request.session["guru_cart"]
        for k, v in cart.items():
            os = OfferedService.objects.get(serviceID = k)
            sub_total = float(os.price)*float(v)
            total += sub_total
            services.append((os, v, sub_total))
    except:
        pass
    return render_to_response('checkout.html',
        {
            "user" : request.user,
            "services" : services,
            "limit_quantity": [i for i in range(1, 10)],
            "total" : total
        },
        context_instance=RequestContext(request)
    )

@login_required(login_url='/login/')
def editservice(request, serv_id):
    service = OfferedService.objects.get(serviceID = serv_id)
    if request.POST:
        edit_service_form = EditServiceForm(request.POST, request.FILES)
        if edit_service_form.is_valid():
            service_title = edit_service_form.cleaned_data['service_title']
            service_type = edit_service_form.cleaned_data['service_type']
            service_is_company = eval(edit_service_form.cleaned_data['service_is_company'])
            service_company_name = edit_service_form.cleaned_data['service_company_name']
            service_account = edit_service_form.cleaned_data['service_account']
            service_price = edit_service_form.cleaned_data['service_price']
            service_price_delimiter = edit_service_form.cleaned_data['service_price_delimiter']
            service_state = edit_service_form.cleaned_data['service_state']
            service_city = edit_service_form.cleaned_data['service_city']
            try:
                service_image = request.FILES['service_image']
            except:
                service_image = service.service_image
            service_brief_desc =  edit_service_form.cleaned_data['service_brief_desc']
            service_description = edit_service_form.cleaned_data['service_description']
            service_email = edit_service_form.cleaned_data['service_email']
            service_telephone = edit_service_form.cleaned_data['service_telephone']

            user_email = request.user.username

            if service_title:
                service.title = service_title
            if service_type:
                service.service_type = service_type
            service.company = service_is_company
            if service_company_name:
                service.company_name = service_company_name
            if service_account:
                service.account = service_account
            if service_price:
                service.price = service_price
            if service_price_delimiter:
                service.price_delimiter = service_price_delimiter
            if service_state:
                service.state = service_state
            if service_city:
                service.city =service_city
            if service_image:
                service.service_image = service_image
            if service_brief_desc:
                service.brief_description = service_brief_desc
            if service_description:
                service.description = service_description
            if service_email:
                service.service_email = service_email
            if service_telephone:
                service.telephone = service_telephone
            service.save()
            message = "<h5>¡Modificación exitosa!</h5>"
            return render_to_response('editservice.html',
                {
                    "return_message": message,
                    "service" : service,
                    "service_types" : SERVICE_TYPES,
                    "price_delimiters" : PRICE_DELIMITER,
                    "states" : STATE,
                    "cities" : CITY,
                    "edit_service_form" : edit_service_form
                },
                context_instance=RequestContext(request)
            )
    else:
        edit_service_form = EditServiceForm()

    return render_to_response('editservice.html',
        {"user": request.user,
        "service" : service,
        "service_types" : SERVICE_TYPES,
        "price_delimiters" : PRICE_DELIMITER,
        "states" : STATE,
        "cities" : CITY,
        "edit_service_form" : edit_service_form},
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
    services = OfferedService.objects.filter(user_email_id = request.user.id)
    return render_to_response('myservices.html',
        {"services" : services,
        "price_delimiter": PRICE_DELIMITER,
        "user": request.user},
        context_instance=RequestContext(request)
    )

@login_required(login_url='/login/')
def offerservice(request):
    if request.POST:
        add_service_form = AddServiceForm(request.POST, request.FILES)
        if add_service_form.is_valid():
            service_title = add_service_form.cleaned_data['service_title']
            service_type = add_service_form.cleaned_data['service_type']
            service_is_company = eval(add_service_form.cleaned_data['service_is_company'])
            service_company_name = add_service_form.cleaned_data['service_company_name']
            service_account = add_service_form.cleaned_data['service_account']
            service_price = add_service_form.cleaned_data['service_price']
            service_price_delimiter = add_service_form.cleaned_data['service_price_delimiter']
            service_state = add_service_form.cleaned_data['service_state']
            service_city = add_service_form.cleaned_data['service_city']
            service_image = request.FILES['service_image']
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
                description = service_description,
                service_email = service_email,
                telephone = service_telephone
            )
            service.save()

            message = "<br/><h4>¡Gracias por crear un servicio!</h4>"
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
    return HttpResponseRedirect('/account')

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
            message = "<br/><h4>Gracias por convertirte en Gurú!</h4>"
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

def refresh_buy(request):
    if request.POST:
        sale_id = request.POST['sale_id']
        purchased = PurchasedService.objects.get(purchased_service_id = sale_id)
        purchased.status = 2
        purchased.save()
    return HttpResponse("Done")

def refresh_rating(request):
    if request.POST:
        rating = request.POST['rating']
        sale_id = request.POST['sale_id']
        purchased = PurchasedService.objects.get(purchased_service_id = sale_id)
        purchased.rating = rating
        purchased.status = 3
        purchased.save()

        specific_service = PurchasedService.objects.get(purchased_service_id = sale_id).seller_email
        services_avg = PurchasedService.objects.filter(seller_email = specific_service).aggregate(Avg('rating'))
        os = OfferedService.objects.get(serviceID = specific_service.serviceID)
        os.rating=int(services_avg['rating__avg'])
        os.save()

    return HttpResponse("Done")

def refresh_sale(request):
    if request.POST:
        purchased_id = request.POST['purchased_id']
        purchased = PurchasedService.objects.get(purchased_service_id = purchased_id)
        purchased.status = 1
        purchased.save()
    #refresh page
    return HttpResponse("Done")

def remove_from_cart(request):
    if request.POST:
        service_id = request.POST['service_id']
        request.session["guru_cart"][service_id] = 0
        # use del request.session["guru_cart"][service_id] if you want to remove totally from cart
    request.session.modified = True
    return HttpResponse("Done")

@login_required(login_url='/login/')
def saleshistory(request):
    myservices = OfferedService.objects.filter(user_email=request.user)
    services = PurchasedService.objects.filter(seller_email = myservices)
    return render_to_response('saleshistory.html',
        {"user": request.user,
        "services" : services,
        "status": VALID_STATES_OPTIONS},
        context_instance=RequestContext(request)
    )

def filter_search(request):
    if not request.POST:
        return HttpResponse("")
    check_company = eval(request.POST["check_company"].capitalize())
    check_freelance = eval(request.POST["check_freelance"].capitalize())
    city = request.POST["city"]
    order_service = request.POST["order_service"]
    service_type = request.POST["service_type"]
    if order_service == u"price":
        order_service = "price"
    elif order_service == u"rating":
        order_service = "-rating"
    if city != u"0":
        if order_service != "0":
            b = 1
            services = OfferedService.objects.filter(service_type = service_type, city = city).order_by(order_service)
        else:
            b = 2
            services = OfferedService.objects.filter(service_type = service_type, city = city)
    else:
        if order_service != "0":
            b = 3
            services = OfferedService.objects.filter(service_type = service_type).order_by(order_service)
        else:
            b = 4
            services = OfferedService.objects.filter(service_type = service_type)
    if check_company and not check_freelance:
        services = services.filter(company = True)
    elif not check_company and check_freelance:
        services = services.filter(company = False)
    html = ""
    for service in services:
        html += '<div class="row">'
        html += '<div class="col-md-3">'
        html +=	'<br/>'
        if service.service_image:
            html += '<img id="service_image" name="service_image" width="555" height="370" src="' + settings.MEDIA_URL + service.get_image() + '" class="attachment-post-thumbnail wp-post-image" alt="'+ service.title +'"/>'
        else:
            html += '<img id="service_image" name="service_image" width="555" height="370" src="' + settings.MEDIA_URL + 'offered_service/default.jpg" class="attachment-post-thumbnail wp-post-image" alt="No image"/>'
        html += '</div><div class="col-md-6">'
        html += '<h3 id="service_name" name="service_name"><b>' + service.title + '</b></h3>'
        html += '<p id="service_price" name="service_price">$ ' + str(service.price) + ' x '
        for pd in PRICE_DELIMITER:
            if service.price_delimiter == pd[0]:
                html += pd[1]
        html += '</p> <p id="service_brief" name="service_brief">'
        html += service.brief_description
        html += '</p></div><div class="col-md-3"><br/><br/><br/>'
        html += '<form class="edd_download_purchase_form" method="post">'
        html += '<div class="edd_purchase_submit_wrapper">'
        html += '<a href="/serviceoverview/' + str(service.serviceID) + '" class="edd-add-to-cart button edd-submit"><span class="edd-add-to-cart-label white">Ver</span></a>'
        html += '</div></form></div></div><hr>'
    return HttpResponse(html)

def serviceoverview(request, serv_id):
    service = OfferedService.objects.get(serviceID = serv_id)
    return render_to_response('serviceoverview.html',
        {"service" : service,
        "price_delimiter": PRICE_DELIMITER,
        "location" : CITY},
        context_instance=RequestContext(request)
    )

def servicelist(request, service):
    services = OfferedService.objects.filter(service_type = service).order_by("-rating")
    return render_to_response('servicelist.html',
        {
            "services" : services,
            "service_type" : service,
            "service_types": SERVICE_TYPES,
            "price_delimiter": PRICE_DELIMITER,
            "cities" : CITY,
        },
        context_instance=RequestContext(request)
    )

@login_required(login_url='/login/')
def shophistory(request):
    services = PurchasedService.objects.filter(client_email = request.user)
    return render_to_response('shophistory.html',
        {"user" : request.user,
        "services" : services,
        "status": VALID_STATES_OPTIONS},
        context_instance=RequestContext(request)
    )
