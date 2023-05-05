"""waterinn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'Topic',TopicViewSet)
# router.register(r'repo_yearly',YearlyViewset)
router.register(r'device_info',DeviceViewset)
router.register(r'key_info',keyViewset)
router.register(r'repo_hourly',HourlyViewset)
router.register(r'repo_daily',DailyViewset)
router.register(r'repo_monthly',MonthlyViewset)
router.register(r'graph_info',GraphViewset)
router.register(r'Rwp_state',RwpstateViewset)
router.register(r'Rwp_setting',RwpsettingViewset)
router.register(r'hpp_state',hppstateViewset)
router.register(r'hpp_setting',hppsettingViewset)
router.register(r'cnd_state',cndstateViewset)
router.register(r'cnd_setting',cndsettingViewset)
router.register(r'flowsen_state',flowsenstateViewset)
router.register(r'flowsen_setting',flowsensettingViewset)
router.register(r'panel_state',panelstateViewset)
router.register(r'panel_setting',panelsettingViewset)
router.register(r'atm_state',atmstateViewset)
router.register(r'atm_setting',atmsettingViewset)
# router.register(r'mapping_comp',mappingViewset)
# router.register(r'consen_state',consenstateViewset)
# router.register(r'consen_setting',consensettingViewset)
router.register(r'tap1_setting',tap1settingViewset)
router.register(r'tap2_setting',tap2settingViewset)
router.register(r'tap3_setting',tap3settingViewset)
router.register(r'tap4_setting',tap4settingViewset)
router.register(r'ampv1_setting',ampv1settingViewset)
router.register(r'ampv1_state',ampv1stateViewset)
router.register(r'ampv2_setting',ampv2settingViewset)
router.register(r'ampv2_state',ampv2stateViewset)
router.register(r'ampv3_setting',ampv3settingViewset)
router.register(r'ampv3_state',ampv3stateViewset)
router.register(r'ampv4_setting',ampv4settingViewset)
router.register(r'ampv4_state',ampv4stateViewset)
router.register(r'ampv5_setting',ampv5settingViewset)
router.register(r'ampv5_state',ampv5stateViewset)
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('c',views.on_message)
]
