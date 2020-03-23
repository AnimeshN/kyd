
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import F1, F2, F3, F4, F9LcBlk

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
        return render(request, 'kyd_dashboard/feature5.html')


class FeatureSix(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request,'kyd_dashboard/feature6.html')

class FeatureSeven(LoginRequiredMixin, TemplateView):
	login_url = '/login/'
	redirect_field_name = 'login'
    def get(self,request):
        return render(request,'kyd_dashboard/feature7.html')

class FeatureEight(LoginRequiredMixin, TemplateView):
	login_url = '/login/'
	redirect_field_name = 'login'
    def get(self,request):
       
        return render(request,'kyd_dashboard/feature8.html' )


class FeatureNine(LoginRequiredMixin, TemplateView):
	login_url = '/login/'
	redirect_field_name = 'login'
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
        


