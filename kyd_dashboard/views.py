from django.shortcuts import render
from django.views.generic import TemplateView
from .models import F1, F2, F3, F4
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class KYDDashboardView(TemplateView):
    template_name = "kyd_dashboard/kyd_base.html"

class FeatureOne(TemplateView):
    def get(self,request):
            data = F1.objects.all()
            jsondata = serializers.serialize('json',data)
            return render(request,'kyd_dashboard/feature1.html',{"data":jsondata})

class FeatureTwo(TemplateView):
    def get(self,request):
        oi_data = F2.objects.all()
        oi_jdata = serializers.serialize('json', oi_data)
        return render(request, 'kyd_dashboard/feature2.html', {"oi_data":oi_jdata})

class FeatureThree(TemplateView):
    def get(self,request):
        data = F3.objects.all()
        jsondata = serializers.serialize('json', data)
        return render(request, 'kyd_dashboard/feature3.html', {"poi_data":jsondata})

class FeatureFour(TemplateView):
    def get(self,request):
        data = F4.objects.all()
        jsondata = serializers.serialize('json', data)
        return render(request, 'kyd_dashboard/feature4.html', {"pi_data":jsondata})