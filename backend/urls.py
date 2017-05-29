from views import newEmployee
from django.conf.urls import url


urlpatterns = [
    
    url(r'^admin/$', newEmployee, name='admin'),
]