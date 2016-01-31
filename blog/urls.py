from django.conf.urls import patterns, include, url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = patterns(
    '',
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    #url(r'^about/$', views.BlogAbout.as_view(), name="about"),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),

)