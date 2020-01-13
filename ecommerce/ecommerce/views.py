from django.views.generic import View, TemplateView, ListView, DetailView, FormView, UpdateView, CreateView
from django.views.generic.edit import FormMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.detail import SingleObjectMixin
from django.utils import timezone

from . import models
from . import forms


class ProductListView(ListView):
    model = models.Product
    template_name = "ecommerce/shop_product_col_3.html"


class SingleProductView(DetailView):
    model = models.Product
    template_name = 'ecommerce/shop_single_product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.TestimonialForm()
        context['reviews'] = models.Review.objects.filter(pk=self.kwargs.get('pk'))
        return context

    #model.objects.create(author=me, title='Sample title', text='Test')


class Testimonial(SingleObjectMixin, FormView):
    template_name = 'ecommerce/shop_single_product.html'
    form_class = forms.TestimonialForm
    model = models.Product

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class ProductDetail(View):

    def get(self, request, *args, **kwargs):
        view = SingleProductView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = Testimonial.as_view()
        return view(request, *args, **kwargs)

