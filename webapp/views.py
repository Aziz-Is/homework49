from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Tracker

# Create your views here.


class MainpageView(TemplateView):
    template_name = 'main.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Tracker.objects.all()
        print(context)
        return context


class DetailView(TemplateView):
    template_name = 'detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Tracker.objects.get(pk=context['pk'])
        print(context)
        return context