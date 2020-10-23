from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from django.core import serializers
from django.core.serializers import serialize
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (F1, F2, F3, F4, F5Awc, F5Beat, F5Blk, F5Prjt, FtLcPrjt, FtLcBlk, FtLcBeat, FtRadar1, FtRadar2,
       F6OiBlock, F6OiProject, F6OiBeat, F6OiAwc, 
       F7IycfAw, F7IycfBlock, F7IycfBt, F7IycfProject,
       F8PwProject, F8PwBlock, F8PwBeat, F8PwAwc,
       DistrictBlockWiseGeojson, DistrictProjectWiseGeojson,
       DistrictBeatWiseGeojson, DistrictAwcGeojson, DistrictVillagewiseGeojson,
       F10AwcInfra)


# Create your views here.

class KYDDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "kyd_dashboard/kyd_base.html"
        
        
class F1MsrmntEffcyBlk_post(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def post(self, request):
        dt_name = request.POST['dist_select']   
        fy_name = request.POST['fy_select'] 
        # print("fy_name")  
        # print(fy_name)
        # quarter_S = request.POST['quarter_select']   
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')  
        # data = F1.objects.all().filter(Q(district_n=dt_name) & (Q(month_n=months[0]['month']) | Q(month_n=months[1]['month']) | Q(month_n=months[2]['month'])))
        data = F1.objects.all().filter(Q(district_n=dt_name) & Q(financial_year=fy_name))
        print(data)
        jsondata = serializers.serialize('json',data)

        return render(request,'kyd_dashboard/f1_msrmnt_effcy_blk.html', {'data':jsondata, 'dist_name': dt_name , 'fy': fy_name})


class F1MsrmntEffcyBlk(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name=None, fy=None):
        district_n = request.GET.get('dist_name', dist_name) 
        fy_name = request.GET.get('fy', fy) 
        #data = F1.objects.all().filter(Q(district_n=district_n) & (Q(month_n=months[0]['month']) | Q(month_n=months[1]['month']) | Q(month_n=months[2]['month'])))
        data = F1.objects.all().filter(Q(district_n=district_n)  & Q(financial_year=fy_name))
        jsondata = serializers.serialize('json',data)  
        
        return render(request,'kyd_dashboard/f1_msrmnt_effcy_blk.html', {'data':jsondata, 'dist_name': district_n, 'fy' :fy_name })                      


class F2OtcmIndctrBlk(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None, fy = None):
        district_n = request.GET.get('dist_name', dist_name)
        fy_name = request.GET.get('fy', fy) 
        # quarter_S = request.GET.get('quarter',quarter)
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')
        # data = F2.objects.all().filter(Q(district_n=district_n) & (Q(month_n=months[0]['month']) | Q(month_n=months[1]['month']) | Q(month_n=months[2]['month'])))
        data = F2.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))
        jsondata = serializers.serialize('json',data)
        if district_n=='Amravati':    
            return render(request,'kyd_dashboard/f2_oi_blk_am.html', {'data':jsondata, 'dist_name':district_n, 'fy':fy_name })
        else:      
            return render(request,'kyd_dashboard/f2_oi_blk.html', {'data':jsondata, 'dist_name':district_n, 'fy':fy_name })

class F3PieProject(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None, fy=None):
        district_n = request.GET.get('dist_name', dist_name)
        fy_name = request.GET.get('fy', fy) 
        # quarter_S = request.GET.get('quarter',quarter)
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')
        # data = F3.objects.all().filter(Q(district_n=district_n) & (Q(month_n=months[0]['month']) | Q(month_n=months[1]['month']) | Q(month_n=months[2]['month'])))
        data = F3.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))
        jsondata = serializers.serialize('json',data)

        return render(request,'kyd_dashboard/f3_pie_prjt.html', {'data':jsondata, 'dist_name':district_n, 'fy':fy_name})


class F4DtProfile(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None, fy=None):
        district_n = request.GET.get('dist_name', dist_name)
        fy_name = request.GET.get('fy', fy) 
        # quarter_S = request.GET.get('quarter',quarter)
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')
        # data = F4.objects.all().filter(Q(district_n=district_n) | Q(district_n='Maharashtra') & (Q(month_n=months[0]['month']) | Q(month_n=months[1]['month']) | Q(month_n=months[2]['month'])))
        data = F4.objects.all().filter((Q(district_n=district_n) | Q(district_n='Maharashtra')) & Q(financial_year=fy_name))
        jsondata = serializers.serialize('json',data)

        return render(request,'kyd_dashboard/f4_dt_profile.html', {'data':jsondata, 'dist_name':district_n, 'fy':fy_name})


class F5DtOverview(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None,  fy=None):
        district_n = request.GET.get('dist_name', dist_name)
        fy_name = request.GET.get('fy', fy) 
        # quarter_S = request.GET.get('quarter',quarter)
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')
        Block_data = F5Blk.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))
        Project_data = F5Prjt.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))
        Beat_data = F5Beat.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))
        Awc_data = F5Awc.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))

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

        return render(request,'kyd_dashboard/f5_dt_overview.html', {'context':context, 'dist_name':district_n,  'fy' : fy_name})


class F6OiMap(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None, fy=None):
        district_n = request.GET.get('dist_name', dist_name)
        fy_name = request.GET.get('fy', fy)
        # quarter_S = request.GET.get('quarter',quarter)
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')
        Block_data = F6OiBlock.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))
        Project_data = F6OiProject.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))
        Beat_data = F6OiBeat.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))
        Awc_data = F6OiAwc.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))

        Block_jsondata = serializers.serialize('json', Block_data)
        Project_jsondata = serializers.serialize('json', Project_data)
        Beat_jsondata = serializers.serialize('json', Beat_data)
        Awc_jsondata = serializers.serialize('json', Awc_data)

        
        
        block_geodata = serialize('geojson', DistrictBlockWiseGeojson.objects.all().filter(district = district_n),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','district'))
        project_geodata = serialize('geojson', DistrictProjectWiseGeojson.objects.all().filter(district = district_n),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','project','district'))
        beat_geodata = serialize('geojson', DistrictBeatWiseGeojson.objects.all().filter(district = district_n),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','project','beat_na','district'))
                        
        if district_n == 'Amravati':  
        
            awc_geodata = serialize('geojson', DistrictVillagewiseGeojson.objects.all().filter(district = district_n),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','project','beat_na', 'village','district'))
        else:
            awc_geodata = serialize('geojson', DistrictAwcGeojson.objects.all().filter(district = district_n),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','beat', 'beat_code', 'beat_withc','awc', 'awc_code', 'awc_with_c','district'))

        context = {
            'block_data': Block_jsondata,
            'project_data': Project_jsondata,
            'beat_data': Beat_jsondata,
            'awc_data': Awc_jsondata,
            'blk_geodata':block_geodata,
            'prjt_geodata':project_geodata,
            'bt_geodata':beat_geodata,
            'awc_geodata':awc_geodata,
        }
        if district_n == 'Amravati':  
            return render(request,'kyd_dashboard/f6_oi_map_am.html', {'context':context, 'dist_name':district_n, 'fy' : fy_name})
        else:
            return render(request,'kyd_dashboard/f6_oi_map.html', {'context':context, 'dist_name':district_n, 'fy' : fy_name})


class F7IycfMap(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None, fy=None):
        district_n = request.GET.get('dist_name', dist_name)
        fy_name = request.GET.get('fy', fy)
        # quarter_S = request.GET.get('quarter',quarter)
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')
        Block_data = F7IycfBlock.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))
        Project_data = F7IycfProject.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))
        Beat_data = F7IycfBt.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))
        Awc_data = F7IycfAw.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))

        Block_jsondata = serializers.serialize('json', Block_data)
        Project_jsondata = serializers.serialize('json', Project_data)
        Beat_jsondata = serializers.serialize('json', Beat_data)
        Awc_jsondata = serializers.serialize('json', Awc_data)

        block_geodata = serialize('geojson', DistrictBlockWiseGeojson.objects.all().filter(district = district_n),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','district'))
        project_geodata = serialize('geojson', DistrictProjectWiseGeojson.objects.all().filter(district = district_n),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','project','district'))
        beat_geodata = serialize('geojson', DistrictBeatWiseGeojson.objects.all().filter(district = district_n),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','project','beat_na','district'))
        
        if district_n == 'Amravati':  
        
            awc_geodata = serialize('geojson', DistrictVillagewiseGeojson.objects.all().filter(district = district_n),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','project','beat_na', 'village','district'))
        else:
            awc_geodata = serialize('geojson', DistrictAwcGeojson.objects.all().filter(district = district_n),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','beat', 'beat_code', 'beat_withc','awc', 'awc_code', 'awc_with_c','district'))

        context = {
            'block_data': Block_jsondata,
            'project_data': Project_jsondata,
            'beat_data': Beat_jsondata,
            'awc_data': Awc_jsondata,
            'blk_geodata':block_geodata,
            'prjt_geodata':project_geodata,
            'bt_geodata':beat_geodata,
            'awc_geodata':awc_geodata,
        }

        if district_n=='Amravati': 
            return render(request,'kyd_dashboard/f7_iycf_map_am.html', {'context':context, 'dist_name':district_n, 'fy' : fy_name})
        else:
            return render(request,'kyd_dashboard/f7_iycf_map.html', {'context':context, 'dist_name':district_n, 'fy' : fy_name})


class F8PwMap(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None, fy=None):
        district_n = request.GET.get('dist_name', dist_name)
        fy_name = request.GET.get('fy', fy)
        # quarter_S = request.GET.get('quarter',quarter)
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')
        Block_data = F8PwBlock.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))
        Project_data = F8PwProject.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))
        Beat_data = F8PwBeat.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))
        Awc_data = F8PwAwc.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))

        Block_jsondata = serializers.serialize('json', Block_data)
        Project_jsondata = serializers.serialize('json', Project_data)
        Beat_jsondata = serializers.serialize('json', Beat_data)
        Awc_jsondata = serializers.serialize('json', Awc_data)

        block_geodata = serialize('geojson', DistrictBlockWiseGeojson.objects.all().filter(district = district_n),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','district'))
        project_geodata = serialize('geojson', DistrictProjectWiseGeojson.objects.all().filter(district = district_n),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','project','district'))
        beat_geodata = serialize('geojson', DistrictBeatWiseGeojson.objects.all().filter(district = district_n),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','project','beat_na','district'))
        
        if district_n=='Amravati':  
        
            awc_geodata = serialize('geojson', DistrictVillagewiseGeojson.objects.all().filter(district = district_n),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','project','beat_na', 'village','district'))
        else:
            awc_geodata = serialize('geojson', DistrictAwcGeojson.objects.all().filter(district = district_n),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','beat', 'beat_code', 'beat_withc','awc', 'awc_code', 'awc_with_c','district'))

        context = {
            'block_data': Block_jsondata,
            'project_data': Project_jsondata,
            'beat_data': Beat_jsondata,
            'awc_data': Awc_jsondata,
            'blk_geodata':block_geodata,
            'prjt_geodata':project_geodata,
            'bt_geodata':beat_geodata,
            'awc_geodata':awc_geodata,
        }

        if district_n=='Amravati':  
            return render(request,'kyd_dashboard/f8_pw_map_am.html', {'context':context, 'dist_name':district_n, 'fy' : fy_name})
        else:
            return render(request,'kyd_dashboard/f8_pw_map.html', {'context':context, 'dist_name':district_n, 'fy' : fy_name})


class FtLcBlock(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None, fy = None):
        district_n = request.GET.get('dist_name', dist_name)
        fy_name = request.GET.get('fy', fy)
        # quarter_S = request.GET.get('quarter',quarter)
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')
        data = FtLcBlk.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name)).order_by('month_n')
        jsondata = serializers.serialize('json',data)

        return render(request,'kyd_dashboard/ft_lc_block.html', {'data':jsondata, 'dist_name':district_n, 'fy' : fy_name})


class FtLcProject(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None,  fy = None):
        district_n = request.GET.get('dist_name', dist_name)
        fy_name = request.GET.get('fy', fy)
        # quarter_S = request.GET.get('quarter',quarter)
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')
        data = FtLcPrjt.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name)).order_by('month_n')
        block_list = FtLcPrjt.objects.all().filter(Q(district_n=district_n)).values('block_n').distinct().order_by('block_n')

        jsondata = serializers.serialize('json',data)

        return render(request,'kyd_dashboard/ft_lc_project.html', {'data':jsondata, 'dist_name':district_n, 'blockList': block_list, 'fy' : fy_name })


class FtLcBeats(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None,  fy = None):
        district_n = request.GET.get('dist_name', dist_name)
        fy_name = request.GET.get('fy', fy)
        # quarter_S = request.GET.get('quarter',quarter)
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')
        data = FtLcBeat.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name)).order_by('month_n')
        project_list = FtLcPrjt.objects.all().filter(Q(district_n=district_n)).values('project_n').distinct().order_by('project_n')
        jsondata = serializers.serialize('json',data)

        return render(request,'kyd_dashboard/ft_lc_beat.html', {'data':jsondata, 'dist_name':district_n, 'projectList': project_list, 'fy' : fy_name})


class FtRdr1(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None,  fy = None):
        district_n = request.GET.get('dist_name', dist_name)
        fy_name = request.GET.get('fy', fy)
        # quarter_S = request.GET.get('quarter',quarter)
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')
        data = FtRadar1.objects.all().filter((Q(district_n=district_n) | Q(district_n='Maharashtra')) & Q(financial_year=fy_name))
        dataCheck= FtRadar1.objects.all().filter(district_n = district_n ).order_by('district_n').values('project_n').distinct()
        jsondata = serializers.serialize('json',data)

        return render(request,'kyd_dashboard/ft_radar1.html', {'data':jsondata, 'projectList':dataCheck, 'dist_name':district_n, 'fy' : fy_name})


class FtRdr2(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None, fy = None):
        district_n = request.GET.get('dist_name', dist_name)
        fy_name = request.GET.get('fy', fy)
        # quarter_S = request.GET.get('quarter',quarter)
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')
        data = FtRadar2.objects.all().filter((Q(district_n=district_n) | Q(district_n='Maharashtra')) & Q(financial_year=fy_name))
        dataCheck= FtRadar2.objects.all().filter(district_n = district_n ).order_by('district_n').values('project_n').distinct()
        jsondata = serializers.serialize('json',data)

        return render(request,'kyd_dashboard/ft_radar2.html', {'data':jsondata, 'projectList':dataCheck, 'dist_name':district_n, 'fy' : fy_name})

class F10AWCInfraBlock(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, dist_name = None, fy = None):
        district_n = request.GET.get('dist_name', dist_name)
        fy_name = request.GET.get('fy', fy)
        # quarter_S = request.GET.get('quarter',quarter)
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')
        data = F10AwcInfra.objects.all().filter(Q(district_n=district_n) & Q(financial_year=fy_name))
        jsondata = serializers.serialize('json',data)
        return render(request,'kyd_dashboard/ft_awc_infra.html', {'data':jsondata, 'dist_name':district_n, 'fy' : fy_name})