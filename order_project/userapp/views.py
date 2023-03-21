from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect


from .models import AppUser
from .forms import AppUserCreatingForm


class RegistrationView(generic.CreateView):
    model = AppUser
    template_name = 'userapp/registarion.html'
    form_class = AppUserCreatingForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super(RegistrationView, self).get(request, *args, **kwargs)

