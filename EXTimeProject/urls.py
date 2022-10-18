"""EXTimeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include,path
from ExTime import views as ExTime_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Games', ExTime_views.GameViewSet)
router.register(r'Dev', ExTime_views.DevViewSet)
router.register(r'User', ExTime_views.UserViewSet)
router.register(r'Service', ExTime_views.ServiceViewSet)
router.register(r'Reviews', ExTime_views.ReviewsViewSet)
router.register(r'RScreen', ExTime_views.RScreenViewSet)
router.register(r'SScreen', ExTime_views.SScreenViewSet)
router.register(r'Stype', ExTime_views.STypeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
