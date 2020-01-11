from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic.edit import FormMixin
from django.http import HttpResponse

from . import models
from . import forms


class ProductListView(ListView):
    model = models.Product
    template_name = "ecommerce/shop_product_col_3.html"


class SingleProductView(FormMixin, DetailView):
    model = models.Product
    template_name = "ecommerce/shop_single_product.html"
    form_class = forms.TestimonialForm

