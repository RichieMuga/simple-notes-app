from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class NoteView(LoginRequiredMixin, TemplateView):
    template_name = "note.html"
    login_url = "/accounts/login/"
