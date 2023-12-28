from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.IndexDashboardView.as_view(), name="dashboard")
]

