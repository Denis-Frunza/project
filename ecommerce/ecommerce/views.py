from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Prefetch

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


class ListCart(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        cart = models.Cart.objects.prefetch_related(
            Prefetch('cart_items', to_attr='cart_items_all')).filter(user=request.user, ordered=False)

        context = {
            'object': cart
            }
        return render(self.request, 'ecommerce/shop_checkout.html', context)


def add_to_cart(request, pk):
    product = get_object_or_404(models.Product, pk=pk)

    cart, created = models.Cart.objects.prefetch_related(
        Prefetch('cart_items', to_attr='cart_items_all')).get_or_create(user=request.user, ordered=False)

    if not created:
        product_cart_item = (cart_item for cart_item in cart.cart_items_all if cart_item.product == product)
        product_cart_item = next(product_cart_item, None)

        if product_cart_item:
            if product_cart_item.quantity < product.quantity_per_unit:
                product_cart_item.quantity += 1
                product_cart_item.save()
                return redirect('product-detail', pk=product.pk)
            else:
                raise ValueError

    product_cart_item = models.CartItem(cart=cart, product=product)
    product_cart_item.save()

    return redirect('product-detail', pk=product.pk)
