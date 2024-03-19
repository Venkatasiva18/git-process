import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from secondapp.models import College, Company


class Hello(View):
    def get(self, request):
        return HttpResponse('<h1>Hello This is Class Based View</h1>')
        # return render(request, 'product/templates/index.html')


class TemplateCBV(TemplateView):
    template_name = 'class_based.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'siva'
        context['age'] = 25
        context['first_name'] = "venkat"
        context['last_name'] = "uppala"
        context['date'] = datetime.datetime.now()
        return context


class CollegeListview(ListView):
    # context_object_name = 'college'
    model = College
    # template_name = 'secondapp/templates/secondapp/college_list.html'


class CompanyListView(ListView):
    model = Company


class CompanyDetailView(DetailView):
    model = Company


class CompanyCreateView(CreateView):
    model = Company
    fields = ['name', 'location', 'ceo']


class CompanyUpdateView(UpdateView):
    model = Company
    fields =('name', 'ceo')


class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('companies')

