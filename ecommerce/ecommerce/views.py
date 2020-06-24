from django.views.generic import View, ListView, DetailView, CreateView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

from datetime import datetime

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
        context['reviews'] = models.Review.objects.filter(product_id_id=self.kwargs.get('pk')).all()
        context['reviews_counter'] = models.Review.objects.filter(product_id_id=self.kwargs.get('pk')).count()
        return context


class Testimonial(SingleObjectMixin, FormView):
    template_name = 'ecommerce/shop_single_product.html'
    form_class = forms.TestimonialForm
    model = models.Product

    def get_success_url(self):
        return reverse_lazy('product-detail', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = models.Review.objects.filter(product_id_id=self.kwargs.get('pk')).all()
        context['reviews_counter'] = models.Review.objects.filter(product_id_id=self.kwargs.get('pk')).count()
        return context

    def form_valid(self, form):
        post = models.Review(
            customer_name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            rating=form.cleaned_data['rating'],
            comment=form.cleaned_data['comment'],
            created_at=datetime.now(),
            product_id_id=self.kwargs.get('pk')
            )

        post.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print("the form is invalid, render the invalid form")
        return self.render_to_response(self.get_context_data(form=form))

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


class ListCartItem(ListView):
    model = models.CartItem
    template_name = 'ecommerce/shop_checkout.html'


# class DetailCartItem(DetailView):
#     model = models.CartItem
#     template_name = 'ecommerce/shop_checkout.html'
#
#
class CreateCartItem(CreateView):
    model = models.CartItem
    template_name = 'ecommerce/shop_checkout.html'


def add_to_cart(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    order_item, created = models.CartItem.objects.get_or_create(product=product,
                                                                user=request.user,
                                                                ordered=False
                                                                )
    cart = models.Cart.objects.filter(user=request.user, ordered=False)
    if cart.exists():
        order = cart[0]
        if order.products.filter:
            pass
    else:
        order = models.Cart.objects.create(user=request.user, ordered_at=timezone.now())
        order.products.add(order_item)
    return redirect('product-detail', pk=pk)
