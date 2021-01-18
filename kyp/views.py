from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core import serializers
from django.core.serializers import serialize
from django.db.models import Q
from .models import DhmtVtGp, DhamtariGplevelGeojson

# Create your views here.

class KypDashboard(LoginRequiredMixin, TemplateView):
    template_name = "kyp/vjty_template.html"


class VtTyGp(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request):
        # Block_data = F6OiBlock.objects.all()
        # Beat_data = F6OiBeat.objects.all()
        gp_data = DhmtVtGp.objects.all()

        # Beat_jsondata = serializers.serialize('json', Beat_data)
        # Block_jsondata = serializers.serialize('json', Block_data)
        gp_jsondata = serializers.serialize('json', gp_data)
        
        # block_geodata = serialize('geojson', DistrictBlockWiseGeojson.objects.all(),
        #                         geometry_field = 'wkb_geometry',
        #                         fields = ('block','district'))
        gp_geodata = serialize('geojson', DhamtariGplevelGeojson.objects.all(),
                                geometry_field = 'wkb_geometry',
                                fields = ('block','gp','pk','district'))

        # beat_geodata = serialize('geojson', DistrictBeatWiseGeojson.objects.all().filter(district = district_n),
        #                         geometry_field = 'wkb_geometry',
        #                         fields = ('block','project','beat_na','district'))
                        
       
        context = {
            # 'block_data': Block_jsondata,
            # 'project_data': Project_jsondata,
            'gp_data': gp_jsondata,
            # 'blk_geodata':block_geodata,
            # 'prjt_geodata':project_geodata,
            'gp_geodata':gp_geodata,
        }
        
        return render(request,'kyp/vajan_tyohar_gp.html', {'context':context}) 