from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='index.html')),
    url(r'^Hi$', views.Hi, name='Hi'),
]