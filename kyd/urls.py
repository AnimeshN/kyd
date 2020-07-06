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
from kyd_dashboard.views import (KYDDashboardView, 
    F1MsrmntEffcyBlk, F1MsrmntEffcyBlk_post, F2OtcmIndctrBlk, F4DtProfile,
    F3PieProject, F5DtOverview, F6OiMap, F7IycfMap, F8PwMap,
    FtLcBlock, FtLcProject, FtLcBeats, FtRdr1, FtRdr2, F10AWCInfraBlock)
from maha_dashboard.views import (MahaFeatureOne_post, MahaFeatureOne, MahaFeatureTwo, MahaFeatureThree,
 MahaFeatureFour, MahaFeatureFive, MahaFeatureSix,MahaFeatureSeven,MahaFeatureEight,MahaFeatureNine,
MahaFeatureStOw, MahaFeatureLCDT, MahaFeatureLCSDT)
from django.conf import settings
from django.conf.urls.static import static
from dashboard import views

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='home'),
    url(r'^kyd_dashboard$', KYDDashboardView.as_view(), name='kyd_dashboard'),
    url(r'^kyd_dashboard/f1_msrmnt_effcy_blk$', F1MsrmntEffcyBlk_post.as_view(), name='f1'),
    url(r'^(?P<dist_name>\w+)/(?P<quarter>\w+)/kyd_dashboard/f1_msrmnt_effcy_blk/$', F1MsrmntEffcyBlk.as_view(), name='f1'),
    url(r'^(?P<dist_name>\w+)/(?P<quarter>\w+)/kyd_dashboard/f2_oi_blk$', F2OtcmIndctrBlk.as_view(), name='f2'),
    url(r'^(?P<dist_name>\w+)/(?P<quarter>\w+)/kyd_dashboard/f3_pie_prjt$', F3PieProject.as_view(), name='f3'),
    url(r'^(?P<dist_name>\w+)/(?P<quarter>\w+)/kyd_dashboard/f4_dt_profile$', F4DtProfile.as_view(), name='f4'),
    url(r'^(?P<dist_name>\w+)/(?P<quarter>\w+)/kyd_dashboard/f5_dt_overview$', F5DtOverview.as_view(), name='f5'),
    url(r'^(?P<dist_name>\w+)/(?P<quarter>\w+)/kyd_dashboard/f6_oi_map$', F6OiMap.as_view(), name='f6'),
    url(r'^(?P<dist_name>\w+)/(?P<quarter>\w+)/kyd_dashboard/f7_iycf_map$', F7IycfMap.as_view(), name='f7'),
    url(r'^(?P<dist_name>\w+)/(?P<quarter>\w+)/kyd_dashboard/f8_pw_map$', F8PwMap.as_view(), name='f8'),
    url(r'^(?P<dist_name>\w+)/(?P<quarter>\w+)/kyd_dashboard/ft_lc_block$', FtLcBlock.as_view(), name='ftlcblk'),
    url(r'^(?P<dist_name>\w+)/(?P<quarter>\w+)/kyd_dashboard/ft_lc_project$', FtLcProject.as_view(), name='ftlcprjt'),
    url(r'^(?P<dist_name>\w+)/(?P<quarter>\w+)/kyd_dashboard/ft_lc_beat$', FtLcBeats.as_view(), name='ftlcbt'),
    url(r'^(?P<dist_name>\w+)/(?P<quarter>\w+)/kyd_dashboard/ft_radar1$', FtRdr1.as_view(), name='ftrdr1'),
    url(r'^(?P<dist_name>\w+)/(?P<quarter>\w+)/kyd_dashboard/ft_radar2$', FtRdr2.as_view(), name='ftrdr2'),
    url(r'^(?P<dist_name>\w+)/(?P<quarter>\w+)/kyd_dashboard/ft_awc_infra$', F10AWCInfraBlock.as_view(), name='ftAwcInfra'),
    
    url(r'^maha_dashboard/maha_feature1$', MahaFeatureOne_post.as_view(), name='maha-feat1'),
    url(r'^(?P<quarter>\w+)/maha_dashboard/maha_feature1$', MahaFeatureOne.as_view(), name='maha-feat1'),
    url(r'^(?P<quarter>\w+)/maha_dashboard/maha_feature2$', MahaFeatureTwo.as_view(), name='maha-feat2'),
    url(r'^(?P<quarter>\w+)/maha_dashboard/maha_feature3$', MahaFeatureThree.as_view(), name='maha-feat3'),
    url(r'^(?P<quarter>\w+)/maha_dashboard/maha_feature4$', MahaFeatureFour.as_view(), name='maha-feat4'), #radar1
    url(r'^(?P<quarter>\w+)/maha_dashboard/maha_feature5$', MahaFeatureFive.as_view(), name='maha-feat5'), #radar2
    url(r'^(?P<quarter>\w+)/maha_dashboard/maha_feature6$', MahaFeatureSix.as_view(), name='maha-feat6'), 
    url(r'^(?P<quarter>\w+)/maha_dashboard/maha_feat6so$',  MahaFeatureStOw.as_view(), name='maha-feat6so'), 
    url(r'^(?P<quarter>\w+)/maha_dashboard/maha_feature7$', MahaFeatureSeven.as_view(), name='maha-feat7'), 
    url(r'^(?P<quarter>\w+)/maha_dashboard/maha_feature8$', MahaFeatureEight.as_view(), name='maha-feat8'), 
    url(r'^(?P<quarter>\w+)/maha_dashboard/maha_feature9$', MahaFeatureNine.as_view(), name='maha-feat9'), 
    url(r'^(?P<quarter>\w+)/maha_dashboard/maha_feat_lcdt$', MahaFeatureLCDT.as_view(), name='maha-feat_lcdt'), 
    url(r'^(?P<quarter>\w+)/maha_dashboard/maha_feat_lcsdt$', MahaFeatureLCSDT.as_view(), name='maha-feat_lcsdt'), 


    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login_request, name='login'),
    url(r'^logout/', views.logout_request, name='logout'),


    # url(r'logout', views.logout_request, name="logout"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
