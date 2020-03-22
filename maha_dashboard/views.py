from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.

class MahaFeatureOne(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request,'maha_dashboard/maha_feat1.html')


class MahaFeatureTwo(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request,'maha_dashboard/maha_feat2.html')


class MahaFeatureThree(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request,'maha_dashboard/maha_feat3.html')


class MahaFeatureFour(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request,'maha_dashboard/maha_feat4.html')


class MahaFeatureFive(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request,'maha_dashboard/maha_feat5.html')

class MahaFeatureSix(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request,'maha_dashboard/maha_feat6.html')


class MahaFeatureSeven(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request,'maha_dashboard/maha_feat7.html')