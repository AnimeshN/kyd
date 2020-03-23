"""kyd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.conf.urls import url
from dashboard.views import DashboardView
from kyd_dashboard.views import (KYDDashboardView, FeatureOne, 
    FeatureTwo, FeatureThree, FeatureFour,FeatureFive, FeatureSix,
    FeatureSeven, FeatureEight, FeatureNine,FeatureTen, 
    FeatureEleven, FeatureComp, FeatureRadar, FeatureRadar2)
from maha_dashboard.views import (MahaFeatureOne, MahaFeatureTwo, MahaFeatureThree,
 MahaFeatureFour, MahaFeatureFive, MahaFeatureSix,MahaFeatureSeven,MahaFeatureEight,MahaFeatureNine)
from django.conf import settings
from django.conf.urls.static import static
from dashboard import views

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='home'),
    url(r'^kyd_dashboard$', KYDDashboardView.as_view(), name='kyd_dashboard'),
    url(r'^kyd_dashboard/feature1$', FeatureOne.as_view(), name='feat1'),
    url(r'^kyd_dashboard/feature2$', FeatureTwo.as_view(), name='feat2'),
    url(r'^kyd_dashboard/feature3$', FeatureThree.as_view(), name='feat3'),
    url(r'^kyd_dashboard/feature4$', FeatureFour.as_view(), name='feat4'),
    url(r'^kyd_dashboard/feature5$', FeatureFive.as_view(), name='feat5'),
    url(r'^kyd_dashboard/feature6$', FeatureSix.as_view(), name='feat6'),
    url(r'^kyd_dashboard/feature7$', FeatureSeven.as_view(), name='feat7'),
    url(r'^kyd_dashboard/feature8$', FeatureEight.as_view(), name='feat8'),
    url(r'^kyd_dashboard/feature9$', FeatureNine.as_view(), name='feat9'),
    url(r'^kyd_dashboard/feature10$', FeatureTen.as_view(), name='feat10'),
    url(r'^kyd_dashboard/feature11$', FeatureEleven.as_view(), name='feat11'),
    url(r'^kyd_dashboard/feature_comp$', FeatureComp.as_view(), name='feat-comp'),
    url(r'^kyd_dashboard/feature_radar$', FeatureRadar.as_view(), name='feat-radar'),
    url(r'^kyd_dashboard/feature_radar2$', FeatureRadar2.as_view(), name='feat-radar2'),
    
    url(r'^maha_dashboard/maha_feature1$', MahaFeatureOne.as_view(), name='maha-feat1'),
    url(r'^maha_dashboard/maha_feature2$', MahaFeatureTwo.as_view(), name='maha-feat2'),
    url(r'^maha_dashboard/maha_feature3$', MahaFeatureThree.as_view(), name='maha-feat3'),
    url(r'^maha_dashboard/maha_feature4$', MahaFeatureFour.as_view(), name='maha-feat4'), #radar1
    url(r'^maha_dashboard/maha_feature5$', MahaFeatureFive.as_view(), name='maha-feat5'), #radar2
    url(r'^maha_dashboard/maha_feature6$', MahaFeatureSix.as_view(), name='maha-feat6'), 
    url(r'^maha_dashboard/maha_feature7$', MahaFeatureSeven.as_view(), name='maha-feat7'), 
    url(r'^maha_dashboard/maha_feature8$', MahaFeatureEight.as_view(), name='maha-feat8'), 
    url(r'^maha_dashboard/maha_feature9$', MahaFeatureNine.as_view(), name='maha-feat9'), 


    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login_request, name='login'),
    url(r'^logout/', views.logout_request, name='logout'),


    # url(r'logout', views.logout_request, name="logout"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

