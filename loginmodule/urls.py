from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.urls import path

from django.conf.urls import url
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    path('loginmodule/', include('loginmodule.urls')),
]
