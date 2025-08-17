from empresa.models import Empresa
from clima.models import Clima
from mensajes.models import Mensajes
from django.db.models import Avg, Sum, Max, Min
import datetime


def empresas_por_estacion(estacion_id):
    return Empresa.objects.all().filter(estacion_id=estacion_id)


def clasificar_dia(id):
    nwclima = Clima.objects.get(id=id)
    if (
        nwclima.temperatura_maxima == None
        or nwclima.temperatura_media == None
        or nwclima.temperatura_minima == None
        or nwclima.precipitacion == None
    ):
        nwclima.favorable = -1
    else:
        # Ultimos 6 dias validos
        six_days = (
            Clima.objects.filter(estacion_id=nwclima.estacion.num_estacion)
            .order_by("fecha")
            .reverse()
        )

        if len(six_days) < 6:
            nwclima.favorable = -1
        else:
            six_days = six_days[:6]
            five_days = six_days[:5]

            dif = True
            for i in range(1, 6):
                if (six_days[i].fecha - six_days[i - 1].fecha).days > 2:
                    dif = False
                    break
            if not dif:
                nwclima.favorable = -1
            else:
                total_prec = 0
                for day in six_days:
                    total_prec += day.precipitacion

                tmin = nwclima.temperatura_minima
                tmax = nwclima.temperatura_maxima
                avg_tm = 0
                for day in five_days:
                    avg_tm += day.temperatura_media
                avg_tm = float(avg_tm) / 5.0
                fav = 0
                if total_prec >= 24.5 and tmin > 7.0 and tmax < 30.0 and avg_tm <= 25.0:
                    fav = 1
                else:
                    fav = 0
                nwclima.favorable = fav
    nwclima.save()


def severidad(id):
    nwclima = Clima.objects.get(id=id)
    hr90 = nwclima.horas_hr_90
    tmed = nwclima.temperatura_media_hr_90
    sev = 0
    if hr90 is None or tmed is None:
        sev = -1
    elif tmed <= 11.6:
        if hr90 <= 15:
            sev = 0
        elif hr90 > 15 and hr90 <= 18:
            sev = 1
        elif hr90 > 18 and hr90 <= 21:
            sev = 2
        elif hr90 > 21 and hr90 <= 24:
            sev = 3
        else:
            sev = 4
    elif tmed > 11.6 and tmed <= 15.0:
        if hr90 <= 12:
            sev = 0
        elif hr90 > 12 and hr90 <= 15:
            sev = 1
        elif hr90 > 15 and hr90 <= 18:
            sev = 2
        elif hr90 > 18 and hr90 <= 21:
            sev = 3
        else:
            sev = 4
    else:
        if hr90 <= 9:
            sev = 0
        elif hr90 > 9 and hr90 <= 12:
            sev = 1
        elif hr90 > 12 and hr90 <= 15:
            sev = 2
        elif hr90 > 15 and hr90 <= 18:
            sev = 3
        else:
            sev = 4
    nwclima.severidad = sev
    nwclima.save()


def deteccion_inicial(id):

    nwclima = Clima.objects.get(id=id)
    # Ultimos 6 dias validos
    six_days = (
        Clima.objects.filter(estacion_id=nwclima.estacion.num_estacion)
        .order_by("fecha")
        .reverse()
    )
    # Comprobando que existan 6 dias validos
    if len(six_days) < 6:
        nwclima.deteccion_inicial = 0
    else:
        six_days = six_days[:6]
        # Comprobando que la diferencia no fue mas de 3 dias
        dif = True
        for i in range(1, 6):
            if (six_days[i].fecha - six_days[i - 1].fecha).days > 2:
                dif = False
                break
        if not dif or (nwclima.fecha - six_days[1].fecha).days < 0:
            nwclima.deteccion_inicial = 0

        elif (nwclima.fecha - six_days[1].fecha).days > 60:
            nwclima.deteccion_inicial = 0

        else:
            if six_days[1].deteccion_inicial > 0:
                nwclima.deteccion_inicial = (
                    six_days[1].deteccion_inicial
                    + (nwclima.fecha - six_days[1].fecha).days
                )
            else:
                sev = 0
                favs = 0
                for clima in six_days:
                    if clima.severidad != -1:
                        sev += clima.severidad
                    if clima.favorable != -1:
                        favs += clima.favorable
                if sev > 17 or favs == 6:
                    nwclima.deteccion_inicial = 1
                else:
                    nwclima.deteccion_inicial = 0
    nwclima.save()


def buscar_senal(acum_severidad, dias_fav, variedad):

    senales = {
        -1: "No aspersion",
        0: "Alerta de tizón",
        1: "Aspersión cada 7 días",
        2: "Aspersión cada 5 días",
    }

    if dias_fav < 5:
        if acum_severidad <= 3:
            return senales[-1]
        elif acum_severidad == 4:
            if variedad == "arrosetada":
                return senales[1]
            return senales[0]
        elif acum_severidad == 5:
            if variedad == "rastrero":
                return senales[2]
            return senales[1]
        elif acum_severidad == 6:
            return senales[1]
        else:
            return senales[2]
    else:
        if acum_severidad < 3:
            return senales[-1]
        elif acum_severidad == 3:
            return senales[0]
        elif acum_severidad == 4:
            if variedad == "arrosetada":
                return senales[2]
            return senales[1]
        else:
            return senales[2]


def ultima_alerta(id_empresa):
    sol = (
        Mensajes.objects.all()
        .filter(tipodemensaje="A")
        .filter(destinatario__empresa=id_empresa)
        .order_by("created_at")
        .reverse()
    )
    print(sol)
    if len(sol) == 0:
        return None
    return sol[0].created_at


def tipo_diagnostico():
    today = datetime.datetime.today()
    year = today.year
    dec_month = today.month
    start, end = 0, 0
    if dec_month > 7:
        start = datetime.date(year, 8, 1)
        end = datetime.date(year + 1, 8, 1)
    else:
        start = datetime.date(year - 1, 8, 1)
        end = datetime.date(year, 8, 1)
    return (
        Clima.objects.filter(fecha__gt=start)
        .filter(fecha__lt=end)
        .filter(deteccion_inicial__gt=1)
        .exists()
    )
