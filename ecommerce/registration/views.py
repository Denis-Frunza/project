from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms


class SignUp(CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('product-list')
    template_name = 'login_register.html'

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        print('fail')
        return self.render_to_response(self.get_context_data(form=form))
