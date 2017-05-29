from django.contrib.auth import views as auth_views
from views import newEmployee
from django.conf.urls import url
from django.core.urlresolvers import reverse

urlpatterns = [
    
    url(
        r'^admin/$',
        newEmployee,
        name='admin',
    ),
]