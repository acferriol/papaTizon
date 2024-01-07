from clima.models import Clima
from clima.utils import buscar_senal
from empresa.models import Empresa
from extras.models import Aparicion
from multimedia.forms import GenForm
from datetime import datetime
import datetime

def contextGraph(datos):
    start = datos['fecha_inicio']
    end = datos['fecha_fin']
    dias = (end-start).days+1
    dates = []
    for i in range(0,dias):
        date = (start + datetime.timedelta(days = i))
        if Clima.objects.all().filter(fecha=date).exists():
            dates.append(date.strftime("%Y-%m-%d"))
    dias = len(dates)
    est = Empresa.objects.values('estacion').filter(id=datos['empresa'])
    clima = Clima.objects.values('fecha','estacion','temperatura_media','temperatura_maxima','temperatura_minima','precipitacion').filter(fecha__gte=start).filter(fecha__lte=end).filter(estacion=est[0]['estacion']).order_by('fecha')
    
    ####PRIMER GRAFICO####
    tmax = [(clima[i]['fecha'],clima[i]['temperatura_maxima']) for i in range(len(clima)) if clima[i]['temperatura_maxima'] is not None]
    tmed = [(clima[i]['fecha'],clima[i]['temperatura_media']) for i in range(len(clima)) if clima[i]['temperatura_media'] is not None]
    tmin = [(clima[i]['fecha'],clima[i]['temperatura_minima']) for i in range(len(clima)) if clima[i]['temperatura_minima'] is not None]
    prec = [(clima[i]['fecha'],clima[i]['precipitacion']) for i in range(len(clima)) if clima[i]['precipitacion'] is not None]
    limtmax = [30 for i in range(len(clima))]
    limtmed = [25 for i in range(len(clima))]
    limtmin = [7 for i in range(len(clima))]
    ####SEGUNDO GRAFICO####
    clima = Clima.objects.values('fecha','estacion','favorable','severidad','deteccion_inicial').filter(fecha__gte=start).filter(fecha__lte=end).filter(estacion=est[0]['estacion'])
    if len(clima)==0:
        return {} 
    favs = [clima[i]['favorable'] for i in range(dias)]
    area = []
    area2 = []
    for i in range(dias):
        if clima[i]['deteccion_inicial'] > 1 and clima[i]['deteccion_inicial']<=14:
            area.append(2)
            area2.append((clima[i]['fecha'],2))
        else:
            area.append(0) 
            area2.append((clima[i]['fecha'],0))
    colors1 = []
    for fav in favs:
        if fav==1:
            colors1.append('red')
        elif fav==0:
            colors1.append('green')
        else:
            colors1.append('brown')
    
    sevs = [clima[i]['severidad'] for i in range(dias)]
    
    ####TERCER GRAFICO#####
    deti = Aparicion.objects.values('fecha','empresa').filter(empresa=datos['empresa'])
    colors2 = []
    semanal = []
    for i in range(len(clima)):
        start = i
        i+=6
        if i >= len(clima):
            break
        sev_acum = 0
        fav = 0
        for day in range(start,i):
            if clima[day]['severidad'] > -1:
                sev_acum+=clima[day]['severidad']
            if clima[day]['favorable'] == 1:
                fav+=1
        if clima[i]['deteccion_inicial'] == 0:
            semanal.append((clima[i]['fecha'],0)) #Periodo de Vigilancia
            colors2.append("brown")
        else:
            if clima[i]['deteccion_inicial'] == 1:
                semanal.append((clima[i]['fecha'],1)) #Diagnostico Inicial
                colors2.append("blue")
            else:
                sign = buscar_senal(sev_acum,fav)
                if sign=='No aspersion':
                    semanal.append((clima[i]['fecha'],3)) #No Aspersion
                    colors2.append("green")
                elif sign=='Alerta de tizon':
                    semanal.append((clima[i]['fecha'],4)) #Alerta Tizon
                    colors2.append("yellow")
                elif sign=='Aspersión cada 7 días':
                    semanal.append((clima[i]['fecha'],5)) #Aspersion cada 7 dias 
                    colors2.append("orange")
                else:
                    semanal.append((clima[i]['fecha'],6)) #Aspersion cada 5 dias
                    colors2.append("red")
    if deti[0] is not None and deti[0]['fecha']<=end:
        semanal.append((deti[0]['fecha'],2)) #Registro de Aparicion
        colors2.append("black")
    #######################
    data = {
        'dates':dates,
        'tmax':tmax, 
        'tmed':tmed,
        'tmin':tmin, 
        'limtmax':limtmax, 
        'limtmed':limtmed, 
        'limtmin':limtmin, 
        'prec':prec,
        'favs':favs,
        'sevs':sevs,
        'colors1':colors1,
        'area':area,
        'area2':area2,
        'semanal':semanal,
        'colors2':colors2,
    }
    return data

def set_fechas():
    today = datetime.datetime.today()
    year = today.year
    dec_month = today.month
    start,end = 0,0
    if dec_month > 7:
        start = datetime.date(year,8,1)
        end = datetime.date(year+1,8,1)
    else:
        start = datetime.date(year-1,8,1)
        end = datetime.date(year,8,1)
    return start,end