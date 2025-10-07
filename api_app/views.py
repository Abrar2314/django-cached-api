from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.core.cache import cache
from .models import Item
from .serializers import ItemSerializer

CACHE_TIMEOUT = 300  # 5 minutes

@api_view(['GET'])
def get_items(request):
    cached_data = cache.get('all_items_page_' + str(request.GET.get('page', 1)))
    if cached_data:
        return Response(cached_data)

    items = Item.objects.all()  # Don't use .values() here
    paginator = PageNumberPagination()
    paginator.page_size = 50
    result_page = paginator.paginate_queryset(items, request)
    serializer = ItemSerializer(result_page, many=True)

    cache.set('all_items_page_' + str(request.GET.get('page', 1)), serializer.data, CACHE_TIMEOUT)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def get_item(request, pk):
    cache_key = f'item_{pk}'
    cached_data = cache.get(cache_key)
    if cached_data:
        return Response(cached_data)

    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response({"error": "Item not found"}, status=404)

    serializer = ItemSerializer(item)
    cache.set(cache_key, serializer.data, CACHE_TIMEOUT)
    return Response(serializer.data)
