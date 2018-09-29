from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^snippets/$', views.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^user/$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls')),
]
