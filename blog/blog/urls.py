"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from article.views import (
    NewsView,
    GetView,
    BootStrapView,
    get_name,
    RegistrationView,
    ImageView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^mine/$', NewsView.as_view(), name='my-view'),
    url(r'^mine1/$', GetView.as_view(), name='my-viewl'),
    url(r'^gallery/$', BootStrapView.as_view(), name='my-BootStrapView'),
    url(r'^name/$', get_name.as_view(), name='get_name'),
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),
    url(r'^image/$', ImageView.as_view(), name='image'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
