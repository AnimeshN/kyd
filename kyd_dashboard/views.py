
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import (F1, F2, F3, F4, F5Awc, F5Beat, F5Blk, F5Prjt, FtLcPrjt, FtLcBlk, FtLcBeat, FtRadar1, 
       F6OiBlock, F6OiProject, F6OiBeat, F6OiAwc, 
       F7IycfAw, F7IycfBlock, F7IycfBt, F7IycfProject,
       F8PwProject, F8PwBlock, F8PwBeat, F8PwAwc,
       ConsoChildNdj)
# from .models import 

from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class KYDDashboardView(LoginRequiredMixin, TemplateView):
    # def get(self,request):
        # dt_name = ConsoChildNdj.objects.order_by('district_n').values('district_n').distinct()
    template_name = "kyd_dashboard/kyd_base.html"

class FeatureOne(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    def get(self,request):
        return render(request,'kyd_dashboard/feature1.html')

class FeatureTwo(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request, 'kyd_dashboard/feature2.html')

class FeatureThree(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request, 'kyd_dashboard/feature3.html')

class FeatureFour(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request, 'kyd_dashboard/feature4.html')

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
        return render(request,'kyd_dashboard/feature8.html')


class FeatureNine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        return render(request,'kyd_dashboard/feature9.html')


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
        

class Demo_dd(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request):
        dt_name = ConsoChildNdj.objects.order_by('district_n').values('district_n').distinct()
        # return render(request,'dashboard/dash.html', {'dd_dt_data':dt_name})
        return render(request,'dashboard/demo_dash.html', {'dd_dt_data':dt_name})


class F1MsrmntEffcyBlk_post(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request):
        dt_name = request.GET['dist_select']          
        data = F1.objects.all().filter(district_n = dt_name)                
        jsondata = serializers.serialize('json',data)

        return render(request,'kyd_dashboard/f1_msrmnt_effcy_blk.html', {'data':jsondata, 'dist_name': dt_name})


class F1MsrmntEffcyBlk(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name=None):
        district = request.GET.get('dist_name', dist_name)           
        data = F1.objects.all().filter(district_n = district)
        jsondata = serializers.serialize('json',data)        
        
        return render(request,'kyd_dashboard/f1_msrmnt_effcy_blk.html', {'data':jsondata, 'dist_name': district})                        


class F2OtcmIndctrBlk(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None):
            district_n = request.GET.get('dist_name', dist_name)
            data = F2.objects.all().filter(district_n = district_n)
            jsondata = serializers.serialize('json',data)

            return render(request,'kyd_dashboard/f2_oi_blk.html', {'data':jsondata, 'dist_name':district_n})


class F3PieProject(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None):
            district_n = request.GET.get('dist_name', dist_name)
            data = F3.objects.all().filter(district_n = district_n)
            jsondata = serializers.serialize('json',data)

            return render(request,'kyd_dashboard/f3_pie_prjt.html', {'data':jsondata, 'dist_name':district_n})


class F4DtProfile(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None):
        district_n = request.GET.get('dist_name', dist_name)
        data = F4.objects.all().filter(district_n = district_n) | F4.objects.all().filter(district_n = 'Maharashtra')
        jsondata = serializers.serialize('json',data)

        return render(request,'kyd_dashboard/f4_dt_profile.html', {'data':jsondata, 'dist_name':district_n})


class F5DtOverview(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None):
        district_n = request.GET.get('dist_name', dist_name)
        Block_data = F5Blk.objects.all().filter(district_n = district_n)
        Project_data = F5Prjt.objects.all().filter(district_n = district_n)
        Beat_data = F5Beat.objects.all().filter(district_n = district_n)
        Awc_data = F5Awc.objects.all().filter(district_n = district_n)

        Block_jsondata = serializers.serialize('json', Block_data)
        Project_jsondata = serializers.serialize('json', Project_data)
        Beat_jsondata = serializers.serialize('json', Beat_data)
        Awc_jsondata = serializers.serialize('json', Awc_data)

        context = {
            'block_data': Block_jsondata,
            'project_data': Project_jsondata,
            'beat_data': Beat_jsondata,
            'awc_data': Awc_jsondata
        }

        return render(request,'kyd_dashboard/f5_dt_overview.html', {'context':context, 'dist_name':district_n})


class F6OiMap(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None):
        district_n = request.GET.get('dist_name', dist_name)
        Block_data = F6OiBlock.objects.all().filter(district_n = district_n)
        Project_data = F6OiProject.objects.all().filter(district_n = district_n)
        Beat_data = F6OiBeat.objects.all().filter(district_n = district_n)
        Awc_data = F6OiAwc.objects.all().filter(district_n = district_n)

        Block_jsondata = serializers.serialize('json', Block_data)
        Project_jsondata = serializers.serialize('json', Project_data)
        Beat_jsondata = serializers.serialize('json', Beat_data)
        Awc_jsondata = serializers.serialize('json', Awc_data)

        context = {
            'block_data': Block_jsondata,
            'project_data': Project_jsondata,
            'beat_data': Beat_jsondata,
            'awc_data': Awc_jsondata
        }

        return render(request,'kyd_dashboard/f6_oi_map.html', {'context':context, 'dist_name':district_n})


class F7IycfMap(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None):
        district_n = request.GET.get('dist_name', dist_name)
        Block_data = F7IycfBlock.objects.all().filter(district_n = district_n)
        Project_data = F7IycfProject.objects.all().filter(district_n = district_n)
        Beat_data = F7IycfBt.objects.all().filter(district_n = district_n)
        Awc_data = F7IycfAw.objects.all().filter(district_n = district_n)

        Block_jsondata = serializers.serialize('json', Block_data)
        Project_jsondata = serializers.serialize('json', Project_data)
        Beat_jsondata = serializers.serialize('json', Beat_data)
        Awc_jsondata = serializers.serialize('json', Awc_data)

        context = {
            'block_data': Block_jsondata,
            'project_data': Project_jsondata,
            'beat_data': Beat_jsondata,
            'awc_data': Awc_jsondata
        }

        return render(request,'kyd_dashboard/f7_iycf_map.html', {'context':context, 'dist_name':district_n})

class F8PwMap(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None):
        district_n = request.GET.get('dist_name', dist_name)
        Block_data = F8PwBlock.objects.all().filter(district_n = district_n)
        Project_data = F8PwProject.objects.all().filter(district_n = district_n)
        Beat_data = F8PwBeat.objects.all().filter(district_n = district_n)
        Awc_data = F8PwAwc.objects.all().filter(district_n = district_n)

        Block_jsondata = serializers.serialize('json', Block_data)
        Project_jsondata = serializers.serialize('json', Project_data)
        Beat_jsondata = serializers.serialize('json', Beat_data)
        Awc_jsondata = serializers.serialize('json', Awc_data)

        context = {
            'block_data': Block_jsondata,
            'project_data': Project_jsondata,
            'beat_data': Beat_jsondata,
            'awc_data': Awc_jsondata
        }

        return render(request,'kyd_dashboard/f8_pw_map.html', {'context':context, 'dist_name':district_n})



class FtLcBlock(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None):
            district_n = request.GET.get('dist_name', dist_name)
            data = FtLcBlk.objects.all().filter(district_n = district_n)
            jsondata = serializers.serialize('json',data)

            return render(request,'kyd_dashboard/ft_lc_block.html', {'data':jsondata, 'dist_name':district_n})


class FtLcProject(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None):
            district_n = request.GET.get('dist_name', dist_name)
            data = FtLcPrjt.objects.all().filter(district_n = district_n)
            jsondata = serializers.serialize('json',data)

            return render(request,'kyd_dashboard/ft_lc_project.html', {'data':jsondata, 'dist_name':district_n})


class FtLcBeats(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None):
            district_n = request.GET.get('dist_name', dist_name)
            data = FtLcBeat.objects.all().filter(district_n = district_n)
            jsondata = serializers.serialize('json',data)

            return render(request,'kyd_dashboard/ft_lc_beat.html', {'data':jsondata, 'dist_name':district_n})


class FtRdr1(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None):
            district_n = request.GET.get('dist_name', dist_name)
            # data = FtRadar1.objects.all().filter(district_n = district_n)
            # jsondata = serializers.serialize('json',data)

            return render(request,'kyd_dashboard/ft_radar1.html', {'dist_name':district_n})


class FtRdr2(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None):
            district_n = request.GET.get('dist_name', dist_name)
            # data = FtRadar1.objects.all().filter(district_n = district_n)
            # jsondata = serializers.serialize('json',data)
            return render(request,'kyd_dashboard/ft_radar2.html', {'dist_name':district_n})    