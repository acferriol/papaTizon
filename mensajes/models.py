from django.db import models
from users.models import User
from datetime import datetime

# Create your models here.
TMENSAJE = (("A","Alerta"),("M","Mensaje"),("C","Consulta"))
TALERTA = (("No aspersión","No aspersión"), ("Alerta Tizón","Alerta Tizón"), ("Aspersión cada 7 días","Aspersión cada 7 días"),("Aspersión cada 5 días","Aspersión cada 5 días") )

class Mensajes(models.Model):
    remitente = models.ForeignKey(User,null=False,blank=False,on_delete=models.DO_NOTHING,related_name="remitente")
    mensaje = models.TextField()
    tipodealerta = models.CharField(max_length=30,choices=TALERTA,blank=True,null=True) 
    tipodemensaje = models.CharField(max_length=11, choices=TMENSAJE)
    destinatario = models.ForeignKey(User,null=False,blank=False,on_delete=models.DO_NOTHING,related_name="destinatario")
    recibido = models.BooleanField('Recibido', default=False)
    img = models.FileField(upload_to="media" ,null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.now()) 
    updated_at = models.DateTimeField(default=datetime.now())