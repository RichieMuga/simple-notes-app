from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexDashboardView.as_view(), name="index")
]

