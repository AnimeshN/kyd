from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class KYDDashboardView(TemplateView):
    template_name = "kyd_dashboard/kyd_base.html"


class FeatureOne(TemplateView):
    template_name = "kyd_dashboard/feature1.html"

class FeatureTwo(TemplateView):
    template_name = "kyd_dashboard/feature2.html"