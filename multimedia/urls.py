from django.urls import path
from multimedia.views import dataGraphic, downloadManual
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('downloadManual', login_required(downloadManual),name="downloadManual"),
    path('graficos',login_required(dataGraphic),name="graficos"),
]

