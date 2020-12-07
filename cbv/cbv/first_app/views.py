from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from first_app import models
from django.urls import reverse_lazy
# Create your views here.


# def index_test(request):
#     return HttpResponse("Helllo World")


# class IndexView(View):
#     def get(self, request):
#         return HttpResponse("Hello world Class")


# class er under er func er first parameter self
# class IndexView(TemplateView):
#     template_name = 'first_app/index.htm'
#     # first project er templates folder check kore
#     # kichu na paile app er templates folder a jay

#     def get_context_data(self, **kwargs):
#         # ** variable argument
#         # kwargs menans {'key':value}
#         context = super().get_context_data(**kwargs)
#         # shob argument gula context a rekhe dibe
#         context['sample_text_1'] = "SAmple text 1"
#         context['sample_text_2'] = "Sample 2"
#         return context


# model er shob value eksathe dekhar jonno
class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'first_app/index.htm'


# detail show kore
class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'first_app/musician_details.htm'


# form er kaj kore
class AddMusician(CreateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = models.Musician
    template_name = 'first_app/musician_form.html'


class UpdateMusician(UpdateView):
    fields = ('first_name', 'instrument')
    model = models.Musician
    # jodio by default eitai choose kore
    template_name = 'first_app/musician_form.html'


class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy("first_app:index")
    template_name = 'first_app/delete_musician.html'
