from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.views import TokenViewBase
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.tokens import default_token_generator

from users_api.models import YamdbUser
from users_api.serializers import UserSerializer, MeSerializer, EmailRegistrationSerializer, UserVerificationSerializer
from users_api.permissions import IsYamdbAdmin



class CreateUser(generics.CreateAPIView):
    """
    Create user with POST request with email parameter.
    Wait for email confirmation code.
    """
    # queryset = YamdbUser.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = EmailRegistrationSerializer

    def post(self, request, *args, **kwargs):
        # breakpoint()

        # code = default_token_generator.make_token(user)
        return super().post(request, *args, **kwargs)


class ConfirmUser(generics.CreateAPIView):
    """
    Activate your user with POST request included email and confirmation_code params
    """
    # queryset = YamdbUser.objects.all()
    serializer_class = UserVerificationSerializer
    permission_classes = (AllowAny, )


    def post(self, request, *args, **kwargs):

        # token = AccessToken.for_user(user)

        return super().post(request, *args, **kwargs)



class UsersViewSet(viewsets.ViewSetMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView,):
    """
    Users List (for admin only), Send PATCH request to /api/v1/users/me/
    for editing your user information.
    """
    queryset = YamdbUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsYamdbAdmin, )
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class UserSelf(
    # viewsets.ViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
    # generics.RetrieveAPIView,
):
    serializer_class = MeSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'put', 'patch']
    queryset = YamdbUser.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_object(self):
        # breakpoint()
        return get_object_or_404(YamdbUser, username=self.request.user.username)

    # @action(methods=['get', 'patch'], detail=False,
    #         permission_classes=[IsAuthenticated, IsSelf],
    #         url_path='me', url_name='personal_data')
    # def personal_data(self, request):
    #     pass
    # detail = False


class RegistrationView(generics.CreateAPIView):
    pass
