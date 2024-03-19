from django.shortcuts import render
from crud.models import Beer
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class BeerListView(ListView):
    model = Beer


class BeerDetailView(DetailView):
    model = Beer


class BeerCreateView(CreateView):
    model = Beer
    fields = ['name', 'taste', 'color','price']


class BeerUpdateView(UpdateView):
    model=Beer
    fields = ['taste', 'color', 'price']


class BeerDeleteView(DeleteView):
    model=Beer
    success_url = reverse_lazy('list')



