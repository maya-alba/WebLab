from views import *
from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views


urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^about/', about, name='about'),
    url(r'^account/', account, name='account'),
    url(r'^add_to_cart/', add_to_cart, name='add_to_cart'),
    url(r'^buy/', buy, name='buy'),
    url(r'^categories/', categories, name='categories'),
    url(r'^checkout/', checkout, name='checkout'),
    url(r'^editservice/(?P<serv_id>.*)', editservice, name='editservice'),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
          {'next_page': '/login/'}
    ),
    url(r'^accounts/profile', profile, name='profile'),
    url(r'^myinfoaccount/', myinfoaccount, name='myinfoaccount'),
    url(r'^myservices/', myservices, name='myservices'),
    url(r'^offerservice/', offerservice, name='offerservice'),
    url(r'^register/', register, name='register'),
    url(r'^refresh_buy/', refresh_buy, name='refresh_buy'),
    url(r'^refresh_sale/', refresh_sale, name='refresh_sale'),
    url(r'^refresh_rating/', refresh_rating, name='refresh_rating'),
    url(r'^remove_from_cart/', remove_from_cart, name='remove_from_cart'),
    url(r'^saleshistory/', saleshistory, name='saleshistory'),
    url(r'^filter_search/', filter_search, name='filter_search'),
    url(r'^servicelist/(?P<service>.*)', servicelist, name='servicelist'),
    url(r'^serviceoverview/(?P<serv_id>.*)', serviceoverview, name='serviceoverview'),
    url(r'^shophistory/', shophistory, name='shophistory'),

)
