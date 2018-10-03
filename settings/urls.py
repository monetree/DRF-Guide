
from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from serializers import views

router = routers.DefaultRouter()
router.register('companies',views.CompanyView)
router.register('languages',views.LanguageView)
router.register('frameworks',views.FrameworksView)
router.register('technologies',views.TechnologiesView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
]
