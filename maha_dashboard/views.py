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