from django_filters import rest_framework as filters
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from api.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# class CategoryViewSet(viewsets.ModelViewSet):
#     __basic_fields = ('name', 'menu__name', 'menu__description')
#     queryset = Category.objects.all()
#     serializer_class = CategoryTreeSerializer
#     filter_backends = (filters.DjangoFilterBackend,
#                        SearchFilter, OrderingFilter)
#     filter_fields = __basic_fields
#     search_fields = __basic_fields
