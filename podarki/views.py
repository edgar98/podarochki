from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
# from django.urls import reverse
from django.views import generic
from django.views.generic import FormView

from cart.forms import CartAddProductForm
from podarki.forms import MyForm
from podarki.models import ShopEntry, ShopCart
from django.contrib import auth


def home(request):
    return render(request, 'podarki/index.html')


class ShopListView(generic.ListView):
    model = ShopEntry


class ItemDetailView(generic.DetailView):
    cart_product_form = CartAddProductForm()
    extra_context = {'cart_product_form': cart_product_form}
    model = ShopEntry


class RegisterFormView(FormView):
    # Указажем какую форму мы будем использовать для регистрации наших пользователей, в нашем случае
    # это UserCreationForm - стандартный класс Django унаследованный
    form_class = MyForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = 'accounts/login'

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "podarki/register.html"

    def form_valid(self, form):
        form.save()
        # Функция super( тип [ , объект или тип ] )
        # Возвратите объект прокси, который делегирует вызовы метода родительскому или родственному классу типа .
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)
