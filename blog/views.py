from django.shortcuts import render

# Create your views here.
from django.views import generic
from . import models
from django.http import HttpResponse
from django.template import loader

class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"