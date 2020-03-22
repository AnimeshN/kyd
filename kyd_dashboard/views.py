
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import F1, F2, F3, F4, F51, F6MapBeat ,F6MapBlock ,F6MapProject, F7IycfBlk, F7IycfPrjt, F7IycfBt
from .models import F8PwBlk, F8PwPrjt, F8PwBt, F9LcBlk

from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class KYDDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "kyd_dashboard/kyd_base.html"

class FeatureOne(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    def get(self,request):
            data = F1.objects.all()
            jsondata = serializers.serialize('json',data)
            return render(request,'kyd_dashboard/feature1.html',{"data":jsondata})

class FeatureTwo(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        oi_data = F2.objects.all()
        oi_jdata = serializers.serialize('json', oi_data)
        return render(request, 'kyd_dashboard/feature2.html', {"oi_data":oi_jdata})

class FeatureThree(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        data = F3.objects.all()
        jsondata = serializers.serialize('json', data)
        return render(request, 'kyd_dashboard/feature3.html', {"poi_data":jsondata})

class FeatureFour(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        data = F4.objects.all()
        jsondata = serializers.serialize('json', data)
        return render(request, 'kyd_dashboard/feature4.html', {"pi_data":jsondata})

class FeatureFive(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        data = F51.objects.all()
        jsondata = serializers.serialize('json', data)
        return render(request, 'kyd_dashboard/feature5.html', {"data":jsondata})


class FeatureSix(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request,'kyd_dashboard/feature6.html')

class FeatureSeven(TemplateView):
    def get(self,request):
        beatData = F7IycfBt.objects.all()
        projectData = F7IycfPrjt.objects.all()
        blockData = F7IycfBlk.objects.all()
        jsonBeat = serializers.serialize('json', beatData)
        jsonProject = serializers.serialize('json', projectData)
        jsonBlock = serializers.serialize('json', blockData)
        context = {
            "jsonBeat":jsonBeat,
            "jsonProject":jsonProject,
            "jsonBlock":jsonBlock
            }
        return render(request,'kyd_dashboard/feature7.html',{"context":context}  )

class FeatureEight(TemplateView):
    def get(self,request):
        beatData = F8PwBt.objects.all()
        projectData = F8PwPrjt.objects.all()
        blockData = F8PwBlk.objects.all()
        jsonBeat = serializers.serialize('json', beatData)
        jsonProject = serializers.serialize('json', projectData)
        jsonBlock = serializers.serialize('json', blockData)
        context = {
            "jsonBeat":jsonBeat,
            "jsonProject":jsonProject,
            "jsonBlock":jsonBlock
            }
        return render(request,'kyd_dashboard/feature8.html',{"context":context}  )


class FeatureNine(TemplateView):
    def get(self, request):
        blockData = F9LcBlk.objects.all()
        jsonBlock = serializers.serialize('json', blockData)
       
        return render(request,'kyd_dashboard/feature9.html', {"jsonBlock":jsonBlock}  )

class FeatureTen(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):

        return render(request,'kyd_dashboard/feature10.html')

class FeatureEleven(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request,'kyd_dashboard/feature11.html')

class FeatureComp(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request,'kyd_dashboard/feature_comp.html')


class FeatureRadar(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request,'kyd_dashboard/feat_radar.html')


class FeatureRadar2(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request,'kyd_dashboard/feat_radar2.html')
        


