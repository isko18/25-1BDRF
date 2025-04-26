from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.users.models import User
from apps.users.serializer import UserSerializer, RegisterUserSerializer


class UserMixins(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_serializer_class(self):
        if self.action in ('create',):
            return RegisterUserSerializer
        return UserSerializer