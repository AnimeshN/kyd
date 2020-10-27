from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core import serializers
from django.core.serializers import serialize
from django.db.models import Q
from .models import (Mhf1, Mhf2, Mhf3, Mhf4,
    Mhf5Dt, Mhf5SubDt,
    Mhf6OiDt, Mhf6OiSubDt, Mhf7IycfDt, Mhf7IycfSubDt, Mhf8PwDt, Mhf8PwSubDt,
    MhftLcDt, MhftLcSubDt,
    MhftRdr1, MhftRdr2,
    MhDtGeojson, MhSubdtGeojson,
    QuarterSelect)

# Create your views here.

class MHDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dash_base.html"
    

class MahaFeatureOne_post(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def post(self, request):
        # quarter_S = request.GET.get('quarter',quarter)   
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')  
        fy_name = request.POST['fy_select'] 
        data = Mhf1.objects.all()
        jsondata = serializers.serialize('json', data)
        
        return render(request,'maha_dashboard/maha_feat1.html', {'data':jsondata, 'fy': fy_name})


class MahaFeatureOne(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request, fy= None):
        # quarter_S = request.GET.get('quarter',quarter)   
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')  
        fy_name = request.GET.get('fy', fy) 
        data = Mhf1.objects.all()
        jsondata = serializers.serialize('json', data)
        
        return render(request,'maha_dashboard/maha_feat1.html', {'data':jsondata, 'fy': fy_name})

class MahaFeatureTwo(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request,fy=None):
        # quarter_S = request.GET.get('quarter',quarter)   
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month') 
        fy_name = request.GET.get('fy', fy) 
        data = Mhf2.objects.all()
        jsondata = serializers.serialize('json',data)
        
        return render(request,'maha_dashboard/maha_feat2.html', {'data':jsondata, 'fy': fy_name})


class MahaFeatureThree(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request,fy=None):
        # quarter_S = request.GET.get('quarter',quarter)   
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month') 
        fy_name = request.GET.get('fy', fy) 
        data = Mhf3.objects.all()
        jsondata = serializers.serialize('json',data)
        
        return render(request,'maha_dashboard/maha_feat3.html', {'data':jsondata, 'fy': fy_name})


class MahaFeatureFour(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request,fy=None):
        # quarter_S = request.GET.get('quarter',quarter)   
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')    
        fy_name = request.GET.get('fy', fy) 
        data = MhftRdr1.objects.all()
        dt_list = MhftRdr1.objects.all().order_by('district_n').values('district_n').distinct().exclude(district_n='Maharashtra')
        jsondata = serializers.serialize('json',data)
        
        return render(request,'maha_dashboard/maha_feat4.html', {'data':jsondata, 'dtList':dt_list, 'fy': fy_name})


class MahaFeatureFive(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request,fy=None):
        # quarter_S = request.GET.get('quarter',quarter)   
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')    
        fy_name = request.GET.get('fy', fy) 
        data = MhftRdr2.objects.all()
        dt_list = MhftRdr2.objects.all().order_by('district_n').values('district_n').distinct().exclude(district_n='Maharashtra')
        jsondata = serializers.serialize('json',data)

        return render(request,'maha_dashboard/maha_feat5.html', {'data':jsondata, 'dtList':dt_list, 'fy': fy_name})


class MahaFeatureSix(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request,fy=None):
        # quarter_S = request.GET.get('quarter',quarter)   
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')    
        fy_name = request.GET.get('fy', fy) 
        data = Mhf4.objects.all()
        jsondata = serializers.serialize('json',data)
        
        return render(request,'maha_dashboard/maha_feat6.html', {'data':jsondata, 'fy': fy_name})


class MahaFeatureStOw(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        # quarter_S = request.GET.get('quarter',quarter)   
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')    
        fy_name = request.GET.get('fy', fy) 
        Dt_data = Mhf5Dt.objects.all()
        Sub_Dt_data = Mhf5SubDt.objects.all()
        
        Dt_jsondata = serializers.serialize('json', Dt_data)
        Sub_Dt_jsondata = serializers.serialize('json', Sub_Dt_data)
        
        context = {
            'dt_data': Dt_jsondata,
            'subdt_data': Sub_Dt_jsondata
        }

        return render(request,'maha_dashboard/maha_feat6so.html', {'context':context, 'fy': fy_name})


class MahaFeatureSeven(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        # quarter_S = request.GET.get('quarter',quarter)   
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')
        fy_name = request.GET.get('fy', fy) 
        Dt_data = Mhf6OiDt.objects.all()
        Sub_Dt_data = Mhf6OiSubDt.objects.all()
        
        Dt_jsondata = serializers.serialize('json', Dt_data)
        Sub_Dt_jsondata = serializers.serialize('json', Sub_Dt_data)
        
        dt_geodata = serialize('geojson', MhDtGeojson.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('ogc_fid','district'))
        Sub_dt_geodata = serialize('geojson', MhSubdtGeojson.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','district'))
        context = {
            'dt_data': Dt_jsondata,
            'subdt_data': Sub_Dt_jsondata,
            'dt_geodata': dt_geodata,
            'subdt_geodata': Sub_dt_geodata,
        }

        return render(request,'maha_dashboard/maha_feat7.html', {'context':context, 'fy': fy_name})

class MahaFeatureEight(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        # quarter_S = request.GET.get('quarter',quarter)  
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')
        fy_name = request.GET.get('fy', fy) 
        Dt_data = Mhf7IycfDt.objects.all()
        Sub_Dt_data = Mhf7IycfSubDt.objects.all()
        
        Dt_jsondata = serializers.serialize('json', Dt_data)
        Sub_Dt_jsondata = serializers.serialize('json', Sub_Dt_data)
        
        dt_geodata = serialize('geojson', MhDtGeojson.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('ogc_fid','district'))
        Sub_dt_geodata = serialize('geojson', MhSubdtGeojson.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','district'))

        context = {
            'dt_data': Dt_jsondata,
            'subdt_data': Sub_Dt_jsondata,
            'dt_geodata': dt_geodata,
            'subdt_geodata': Sub_dt_geodata,
        }

        return render(request,'maha_dashboard/maha_feat8.html', {'context':context, 'fy': fy_name})


class MahaFeatureNine(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        # quarter_S = request.GET.get('quarter',quarter)   
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')
        fy_name = request.GET.get('fy', fy) 
        Dt_data = Mhf8PwDt.objects.all()
        Sub_Dt_data = Mhf8PwSubDt.objects.all()
        
        Dt_jsondata = serializers.serialize('json', Dt_data)
        Sub_Dt_jsondata = serializers.serialize('json', Sub_Dt_data)
        
        dt_geodata = serialize('geojson', MhDtGeojson.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('ogc_fid','district'))
        Sub_dt_geodata = serialize('geojson', MhSubdtGeojson.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','district'))

        context = {
            'dt_data': Dt_jsondata,
            'subdt_data': Sub_Dt_jsondata,
            'dt_geodata': dt_geodata,
            'subdt_geodata': Sub_dt_geodata,
        }

        return render(request,'maha_dashboard/maha_feat9.html', {'context':context, 'fy': fy_name})


class MahaFeatureLCDT(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        # quarter_S = request.GET.get('quarter',quarter)   
        # months =  QuarterSelect.objects.filter(quarter=quarter_S).values('month')    
        fy_name = request.GET.get('fy', fy) 
        data = MhftLcDt.objects.all().order_by('month_n')
        jsondata = serializers.serialize('json',data)

        return render(request,'maha_dashboard/maha_feat_lcdt.html', {'data':jsondata, 'fy': fy_name})


class MahaFeatureLCSDT(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self,request,fy=None):
        fy_name = request.GET.get('fy', fy) 
        data = MhftLcSubDt.objects.all().order_by('month_n')
        jsondata = serializers.serialize('json',data)
        district_list = MhftLcSubDt.objects.all().values('district_n').distinct().order_by('district_n')

        return render(request,'maha_dashboard/maha_feat_lcsdt.html', {'data':jsondata, 'districtList': district_list, 'fy': fy_name})
