from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.
from .models import ConsoChildAll, DistrictPwd

class DashboardView(TemplateView):
    def get(self,request):
        username = request.user.username

        if (username == 'admin' or username == 'Maharashtra'):
            dt_name = DistrictPwd.objects.all()
        else:
            dt_name = DistrictPwd.objects.filter(Q(district_n=username) | Q(district_n='Maharashtra'))

        return render(request,'dashboard/dash.html', {'dd_dt_data':dt_name})


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