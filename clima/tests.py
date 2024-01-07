from django.test import TestCase
from users.models import User
from empresa.models import Empresa
from estacion.models import Estacion

# Create your tests here.
class ViewsTestCase(TestCase):
    def setUp(self):
        Estacion.objects.create(num_estacion='123456',nombre='testestacion',provincia='Cienfuegos')
        Empresa.objects.create(nombre='empresatest',estacion_id='123456',representante='Cualquiera',municipio='Santa Clara',provincia='Artemisa')
        self.credentials = {
            'username':'test',
            'password': 'secret',
            'edad':22,
            'empresa_id':1,
            'aprobado':True
        }
        User.objects.create_user(**self.credentials)

    def test_index_loads_properly(self):
        """The login page loads properly"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_clima_lista_clima_loads_properly(self):
        """The list clima page loads properly"""
        response = self.client.post('/accounts/login/?next=/',self.credentials,follow=True)
        self.assertTrue(response.context['user'].is_active)
        
        response = self.client.get('/clima/lista_clima_hoy')
        self.assertEqual(response.status_code, 403)

        response = self.client.get('/mensajes/mensajes_recibidos')
        self.assertEqual(response.status_code, 200)

    def test_register_loads_properly(self):
        """The register page loads properly"""
        response = self.client.get('/users/registrar')
        self.assertEqual(response.status_code, 200)

    def test_clima_lista_hoy_loads_properly(self):
        """The list clima page loads properly"""
        response = self.client.get('/clima/lista_clima_hoy')
        self.assertEqual(response.status_code, 302)
