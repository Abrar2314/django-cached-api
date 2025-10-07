from django.urls import path
from .views import get_items, get_item  # removed get_stats

urlpatterns = [
    path('items/', get_items, name='get_items'),
    path('items/<int:pk>/', get_item, name='get_item'),
    # removed any path pointing to get_stats
]
