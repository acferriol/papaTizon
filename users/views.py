from http.client import HTTPResponse
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import CreateView, ListView,DeleteView,UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from users.models import User 
from users.forms import SignUpForm
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    if request.user.aprobado:
        return render(request,'index_admin.html')
    else:
        return render(request, '401.html')

class RegistroUsuario(CreateView):
    model = User
    template_name = 'user_registro.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(RegistroUsuario,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_normal = True
            user.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class UserList(UserPassesTestMixin,ListView):
    model = User
    template_name = 'listar_usuarios.html'

    def get_queryset(self):
        return User.objects.all().filter(aprobado=0)
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin


class UserDelete(UserPassesTestMixin,DeleteView):
    model = User
    template_name = 'eliminar_usuario.html'
    success_url = reverse_lazy('users:lista_users')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin


class UserAprove(UserPassesTestMixin,UpdateView):
    model = User
    template_name = 'aprobar_usuario.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:lista_users')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_user = kwargs['pk']
        user = self.model.objects.get(id=id_user)
        user.aprobado = True
        user.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin