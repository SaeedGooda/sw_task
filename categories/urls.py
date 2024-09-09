from django.urls import path
from .views import get_subcategories

from .views import category_selector

urlpatterns = [
    path('', category_selector, name='categories'),
    path('get_subcategories/', get_subcategories, name='get_subcategories'),
]
