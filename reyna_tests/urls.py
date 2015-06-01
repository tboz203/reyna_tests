from django.conf.urls import include, url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/(?P<test_pk>[^/]+)/$', views.test_detail, name='test_detail'),
    url(r'^test/(?P<test_pk>[^/]+)/(?P<start>\d+)/$', views.test_detail, name='test_detail'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^post_submission/$', views.post_submission, name='post_submission'),
    url(r'^result/(?P<pk>\d+)/$', views.AttemptDetailView.as_view(), name='attempt_detail'),
    url(r'^results/$', views.AttemptListView.as_view(), name='attempt_list'),
    url(r'^submit/(?P<test_pk>\d+)/$', views.submit, name='submit'),
]

# vim: tw=0
