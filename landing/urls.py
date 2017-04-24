from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^register$', views.register, name='register'),
     url(r'^services', views.services, name='services'),
     url(r'^sitemap', views.sitemap, name='sitemap'),

     url(r'^paralegal', views.paralegal, name='paralegal'),
     url(r'^feedback', views.feedback, name='feedback'),
     url(r'^contact', views.contact, name='contact'),

     url(r'^formation', views.formation, name='formation'),
     url(r'^sole', views.sole, name='sole'),
     url(r'^society', views.society, name='society'),
     url(r'^partnership', views.partnership, name='partnership'),
     url(r'^private', views.private, name='private'),
     url(r'^llp', views.llp, name='llp'),
     url(r'^opc', views.opc, name='opc'),
     url(r'^trust', views.trust, name='trust'),
     url(r'^nidhi', views.nidhi, name='nidhi'),
     url(r'^section8', views.section8, name='section8'),
     url(r'^paraform', views.paraform, name='paraform'),



     ]