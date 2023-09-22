from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import (
    TemplateView,
    DetailView,
    CreateView,
    DeleteView, UpdateView

)
from .models import Person


class HomePageView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    def get(self, request):
        context = {}
        clay = Person.objects.all()
        context['temp'] = clay
        return render(request, 'home.html', {'temp': clay})

    def test_func(self):
        return self.request.user.is_authenticated


class BlogDetailView(DetailView):
    model = Person
    template_name = 'post_detail.html'


class CreatePostView(CreateView):
    model = Person
    template_name = 'new_post.html'
    fields = ['full_name', 'age', 'ish_joyi', 'birthday', 'info']


class BlogDeleteView(DeleteView):
    model = Person
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class BlogUpdateView(UpdateView):
    model = Person
    template_name = 'post_edit.html'
    fields = ['full_name', 'age', 'ish_joyi', 'birthday', 'info'];


# def my_view(request):
#     text = _("English Text")
#     return render(request, 'post_detail.html', {'text': text})
