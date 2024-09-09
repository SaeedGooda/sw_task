from django.http import JsonResponse
from .models import Category
from django.shortcuts import render

def get_subcategories(request):
    parent_id = request.GET.get('parent_id')
    if parent_id:
        subcategories = Category.objects.filter(parent_id=parent_id)
        data = list(subcategories.values('id', 'name'))
        return JsonResponse(data, safe=False)
    return JsonResponse([], safe=False)

def category_selector(request):
    categories = Category.objects.filter(parent__isnull=True)  # Top-level categories
    return render(request, 'categories/categories.html', {'categories': categories})

