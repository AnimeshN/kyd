from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class DashboardView(TemplateView):
    template_name = "dashboard/dash.html"


# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('Hello, World!')