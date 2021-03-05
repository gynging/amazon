from django.shortcuts import render
from django.views import generic
from .models import *

class Lp(generic.TemplateView):
    template_name = 'amazon/lp.html'

    # ここから追加
    def get_context_data(self, **kwargs):
        context = super(Lp, self).get_context_data(**kwargs)
        all_items = Product.objects.all()
        context['items'] = all_items
        return context
    # ここまで追加

class ItemList(generic.ListView):
    model = Product
    template_name = 'amazon/item_list.html'

    def get_queryset(self):
        products = Product.objects.all()
        if 'q' in self.request.GET and self.request.GET['q'] != None:
            q = self.request.GET['q']
            products = products.filter(name__icontains = q)
        return products

## 中略

# [4-2] 商品詳細ビュー追加 ここから
class ItemDetail(generic.DetailView):
    model = Product
    template_name = 'amazon/item_detail.html'
# [4-2] 商品詳細ビュー追加 ここまで
