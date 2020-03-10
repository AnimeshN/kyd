from django.shortcuts import render
from django.views.generic import TemplateView
from .models import F1, F2, F3, F4, F6MapBeat ,F6MapBlock ,F6MapProject
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

class FeatureSix(TemplateView):
    def get(self,request):
        beatData = F6MapBeat.objects.all()
        projectData = F6MapProject.objects.all()
        blockData = F6MapBlock.objects.all()
        jsonBeat = serializers.serialize('json', beatData)
        jsonProject = serializers.serialize('json', projectData)
        jsonBlock = serializers.serialize('json', blockData)
        context = {
            "jsonBeat":jsonBeat,
            "jsonProject":jsonProject,
            "jsonBlock":jsonBlock
            }
        return render(request,'kyd_dashboard/feature5.html',{"context":context}  )