# views.py
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from .pagination import StandardResultsSetPagination
from rest_framework.renderers import JSONRenderer

from .serializers import ProductSerializer
from .models import NikeCrawl


class ProductViewSet(viewsets.ModelViewSet):
    queryset = NikeCrawl.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]