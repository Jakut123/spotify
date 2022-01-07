from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView

from .serializers import RegistrationSerializer, ActivationSerializer, LoginSerializer
from rest_framework.response import Response


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.create()
            return Response('Вы успешно зарегались')


class ActivationView(APIView):
    def post(self, request):
        data = request.data
        serializer = ActivationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.activate()
        return Response('Ваш аккаунт успешно активирован')


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    pass


class ChangePasswordView(APIView):
    pass


class ForgotPasswordView(APIView):
    pass

