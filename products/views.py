#from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView
)
from django.contrib.auth.mixins import  LoginRequiredMixin
from .filters import ProductFilter
from .forms import ProductForm
from .models import Product
from django.views.decorators.csrf import csrf_protect
from .models import Subscription, Category
from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import render

class ProductList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


# Добавляем новое представление для создания товаров.
class ProductCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'

@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscription.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscription.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )
