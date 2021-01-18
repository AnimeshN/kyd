from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db.models import Q
from .models import (DtAvgTable, ConsoChildAll, DistrictPwd)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.core.serializers import serialize
from .serializers import DtAvgTableSerializer
import json
from django.http import JsonResponse


# Create your views here.

def create_post_area(request, fy=None, dist_name=None):
    dist = request.GET.get('dist_name', dist_name) 
    areaSelected = request.GET.get('area')
    monthSelected = request.GET.get('month')
    fy_name = request.GET.get('fy', fy) 
    if areaSelected =='All':
        areaSelected = 'Maharashtra'
    data = DtAvgTable.objects.filter(Q(district_n=areaSelected) & Q(financial_year=fy_name) & Q(month=monthSelected))
    jsondata = json.dumps(DtAvgTableSerializer(data,  many=True).data)
    return JsonResponse({'data':jsondata, 'dist_name': areaSelected})
       

class DashboardView(TemplateView):
    def get(self,request):
        username = request.user.username

        if (username == 'dhamtari'):
            return render(request,'kyp/vjty_template.html')
        else:
            return render(request,'dashboard/dash.html')

class RegionOverview(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    def post(self,request):
        username = request.user.username
        fy_name = request.POST['fy_select']
        if (username == 'admin' or username == 'Maharashtra'):
            dt_name = DistrictPwd.objects.filter(Q(state_n='Maharashtra')).values('district_n').distinct().order_by('district_n')
        else:
            dt_name = DistrictPwd.objects.filter(Q(state_n='Maharashtra') & Q(district_n=username)).values('district_n').distinct()
            block_name = DistrictPwd.objects.filter(Q(state_n='Maharashtra') & Q(district_n=username)).values('block_n').distinct()
       
        if (username == 'admin' or username == 'Maharashtra'):
            district_name = 'Maharashtra'
           
        else:
            district_name =username 
       
        data = DtAvgTable.objects.filter(Q(district_n=district_name) & Q(financial_year=fy_name) & Q(month='All'))
        jsondata = serializers.serialize('json',data)
        return render(request,'dashboard/dt_dashboard.html', {'dd_dt_data':dt_name, 'data':jsondata, 'dist_name':district_name, 'fy': fy_name})



def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "dashboard/login.html",
                    context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")