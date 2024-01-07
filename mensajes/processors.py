from mensajes.models import Mensajes

def ctx_dict(request):
    sol=None
    if request.user.is_authenticated:
        sol = len(Mensajes.objects.filter(recibido=False).filter(destinatario=request.user))
    ctx={'test':sol}
    print(sol)
    return ctx