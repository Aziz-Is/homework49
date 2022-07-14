from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .models import Tracker
from .forms import MyForm

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

class AddView(TemplateView):
    template_name = 'add.html'
    form = MyForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_form'] = self.form()
        return context
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            Tracker.objects.create(summary=form.cleaned_data['summary'], description=form.cleaned_data['description'],
                                   status=form.cleaned_data['status'], type=form.cleaned_data['type'])

            return redirect('home')
        return render(request, 'add.html', {'my_form': form})

class UpdateView(TemplateView):
    template_name = 'add.html'
    form = MyForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Tracker.objects.get(pk=context['pk'])
        context['my_form'] = self.form(initial={'summary':obj.summary, 'description': obj.description, 'status':obj.status, 'type':obj.type})
        return context
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            obj = Tracker.objects.get(pk=kwargs['pk'])
            obj.summary = form.cleaned_data['summary']
            obj.description = form.cleaned_data['description']
            obj.status = form.cleaned_data['status']
            obj.type = form.cleaned_data['type']
            obj.save()
            return redirect('home')
        return render (request, 'add.html',{'my_form':form})

class DeleteView(TemplateView):
    template_name = 'delete.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Tracker.objects.get(pk=context['pk'])
        context['task'] = obj
        return context
    def post(self, request, *args, **kwargs):
        obj = Tracker.objects.get(pk=kwargs['pk'])
        if obj:
            obj.delete()
            return redirect('home')
        return render (request,'delete.html', {'task':obj})
