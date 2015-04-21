from views import *
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^account/', account, name='account'),
    url(r'^categories/', categories, name='categories'),
    url(r'^checkout/', checkout, name='checkout'),
    url(r'^editservice/', editservice, name='editservice'),
    url(r'^login/', login, name='login'),
    url(r'^myinfoaccount/', myinfoaccount, name='myinfoaccount'),
    url(r'^myservices/', myservices, name='myservices'),
    url(r'^offerservice/', offerservice, name='offerservice'),
    url(r'^register/', register, name='register'),
    url(r'^saleshistory/', saleshistory, name='saleshistory'),
    url(r'^servicelist/', servicelist, name='servicelist'),
    url(r'^serviceoverview/', serviceoverview, name='serviceoverview'),
    url(r'^shophistory/', shophistory, name='shophistory'),

)
