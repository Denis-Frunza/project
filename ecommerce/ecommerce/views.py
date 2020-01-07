from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse

from . import models


class ProductListView(ListView):
    model = models.Product
    template_name = "ecommerce/shop_product_col_3.html"


class SingleProductView(DetailView):
    model = models.Product
    template_name = "ecommerce/shop_single_product.html"


# class ProductView(TemplateView):
#     template_name = "ecommerce/product_list.html"

# class ProductView(View):
#     template_name = 'product.html'
#
#     def get(self, request):
#         return HttpResponse('hello World')