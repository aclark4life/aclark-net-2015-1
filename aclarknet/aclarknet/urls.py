from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'aclarknet.aclarknet.views.home', name='home'),
    url(r'^projects', 'aclarknet.aclarknet.views.projects', name='projects'),
    url(r'^services', 'aclarknet.aclarknet.views.services', name='services'),
    url(r'^about/book', 'aclarknet.aclarknet.views.book', name='book'),
    url(r'^about/clients', 'aclarknet.aclarknet.views.clients', name='clients'),
    url(r'^about/history', 'aclarknet.aclarknet.views.history', name='history'),
    url(r'^about/team', 'aclarknet.aclarknet.views.team', name='team'),
    url(r'^about/testimonials', 'aclarknet.aclarknet.views.testimonials', name='testimonials'),
    url(r'^about', 'aclarknet.aclarknet.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact', 'aclarknet.aclarknet.views.contact', name='contact'),
)
