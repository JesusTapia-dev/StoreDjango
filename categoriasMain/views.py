from django.shortcuts import render,get_object_or_404
from item.models import Item,Category

# def categoriasDetail(request,pk):
#     item=get_object_or_404(Item,pk=pk)
#     categorias = Category.objects.all()
#     specificItems=Item.objects.filter(category=item.category,is_sold=False)
#     return render(request, 'categorias/categoriasDetail.html',{
#         'item':item,
#         'categorias':categorias,
#         'specificItems':specificItems,
#         'category': item.category, 
#     })
def categoriasDetail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    items = Item.objects.filter(category=category)
    return render(request, 'categorias/categoriasDetail.html', {
        'category': category, 'items': items
        })