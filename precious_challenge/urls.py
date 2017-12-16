"""precious_challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from trips import views
from trips.serializers import TripSerializer
from trips.models import Trip

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # set the http://127.0.0.1:8000/ url to return one view that lists all trips
    url(r'',views.TripList.as_view(queryset=Trip.objects.all(),serializer_class= TripSerializer),name="trips")
]

