from .serializers import InvoiceSerializer, ItemLineSerializer, User, UserSerializer
from rest_framework.generics import CreateAPIView, ListAPIView


class ClientList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class InvoiceCreate(CreateAPIView):
    serializer_class = InvoiceSerializer
