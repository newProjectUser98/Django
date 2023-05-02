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
# router.register(r'device_info',DeviceViewset)
# router.register(r'key_info',keyViewset)
# router.register(r'repo_hourly',HourlyViewset)
# router.register(r'repo_daily',DailyViewset)
# router.register(r'repo_monthly',MonthlyViewset)
# router.register(r'graph_info',GraphViewset)
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('c',views.on_message)

]
