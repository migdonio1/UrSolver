from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/	
    url(r'^(?P<solver_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<solver_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/registrar/
    url(r'^registrar/$',views.registrar, name='registrar'),
]