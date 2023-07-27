from django.shortcuts import render,get_object_or_404
from item.models import Item,Category

def categoriasDetail(request,pk):
    item=get_object_or_404(Item,pk=pk)
    categories = Category.objects.all()
    return render(request, 'categorias/categoriasDetail.html',{
        'item':item,
        'categories':categories,
    })