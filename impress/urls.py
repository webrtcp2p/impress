from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='impress.html'),name='impress'),
    url(r'^submit$', views.impress,name='impress'),
    url(r'^download', views.download, name="export"),
	
 
]
