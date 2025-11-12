from rest_framework import viewsets
from .models import Ecommerce
from .serializers import EcommerceSerializer

class EcommerceViewSet(viewsets.ModelViewSet):
    queryset = Ecommerce.objects.all()
    serializer_class = EcommerceSerializer
