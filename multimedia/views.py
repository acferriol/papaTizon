from http.client import HTTPResponse
import mimetypes
from django.shortcuts import render,HttpResponse
import os
from pathlib import Path
from clima.models import Clima
from clima.utils import buscar_senal
from empresa.models import Empresa
from extras.models import Aparicion
from multimedia.forms import GenForm
from multimedia.utils import contextGraph,set_fechas
# Create your views here.

def downloadManual(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = "ManualUsuario.pdf"
    filepath = os.path.join(BASE_DIR,'static')
    filepath = os.path.join(filepath,'vendor')
    filepath = os.path.join(filepath,filename)
    path = open(filepath,'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path,content_type= mime_type)
    response['Content-Disposition'] = f"attachment; filename={filename}"
    return response

from django.shortcuts import render
import datetime

# Create your views here.

def dataGraphic(request):
    if request.method == 'POST':
        datos = {} #fecha_inicio, fecha_fin, empresa
        form = GenForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
        else:
            return render(request,'graficos.html',{'form':form})
    else:
        
        defaultEmp = request.user.empresa.id
        defaultfechini, defaultfechfin = set_fechas()
        form = GenForm(initial={'empresa':defaultEmp})
        datos = {
            'empresa':defaultEmp,
            'fecha_inicio': defaultfechini,
            'fecha_fin': defaultfechfin
        }
    data = contextGraph(datos)
    data['form'] = form
    return render(request,'graficos.html',context=data)    
    