from django.shortcuts import render
from item.models import Item, Category
# Create your views here.
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    new_items=Item.objects.filter(is_sold=False).order_by("-created_at")[0:3]

    return render(request, 'core/index.html',{
        'categories':categories,
        'items':items, 
        'new_items':new_items,
    })
def contact(request):
    items=Item.objects.filter(is_sold=False)

    return render(request,'core/contact.html'
                  ,{'items':items
                    })
def product(request):
    items=Item.objects.filter(is_sold=False)
    return render(request,'core/product.html'
                  ,{'items':items
                    })