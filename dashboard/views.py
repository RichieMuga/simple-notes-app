from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class IndexDashboardView(TemplateView):
    template_name = "dashboard.html"
    login_url = "/accounts/login/"
