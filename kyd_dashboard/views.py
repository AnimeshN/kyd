from django.shortcuts import render
from django.views.generic import TemplateView
from .models import F1
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class KYDDashboardView(TemplateView):
    template_name = "kyd_dashboard/kyd_base.html"

class FeatureOne(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    def get(self,request):
            data = F1.objects.all()
            jsondata = serializers.serialize('json',data)
            return render(request,'kyd_dashboard/feature1.html',{"data":jsondata})

class FeatureTwo(TemplateView):
    template_name = "kyd_dashboard/feature2.html"