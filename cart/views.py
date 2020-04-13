# from django.core.exceptions import ObjectDoesNotExist
# from django.shortcuts import render
#
# # Create your views here.
# from cart.models import ShopCart
#
#
# def cart_manager_view(request):
#     if request.method == 'POST':
#         pass
#     else:
#         session = request.session
#         try:
#             cart = session.shopcart
#         except ObjectDoesNotExist:
#             cart = ShopCart(user=user).save()
#             user.shopcart = cart
#             user.save()
#             cart = user.shopcart
#         return render(request, 'podarki/shopcart_list.html', {'object_list': cart.shopcartentry_set.all()})

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from podarki.models import ShopEntry
from .cart import SessionCart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = SessionCart(request)  # create a new cart object passing it the request object
    product = get_object_or_404(ShopEntry, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = SessionCart(request)
    product = get_object_or_404(ShopEntry, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = SessionCart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
