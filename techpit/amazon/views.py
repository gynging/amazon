from django.views import generic
from .models import * # この行を追加

class Lp(generic.TemplateView):
    template_name = 'amazon/lp.html'

# ここから追加
class ItemList(generic.ListView):
    model = Product
    template_name = 'amazon/item_list.html'

    def get_queryset(self):
        products = Product.objects.all()
        if 'q' in self.request.GET and self.request.GET['q'] != None:
            q = self.request.GET['q']
            products = products.filter(name__icontains = q)
        return products
# ここまで追加
