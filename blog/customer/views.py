import hashlib
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import HttpResponseRedirect

from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    GenericAPIView
)

from .serializer import ProfileSerializer
from .models import Profile


class ProfileView(GenericAPIView):
    serializer_class = ProfileSerializer

    queryset = ""

    def get(self, request, activate_code):
        user = Profile.objects.get(activate_code=activate_code)
        if user and user.is_active is False:
            user.is_active = True
            user.save()
            return Response("success")
        else:
            return Response("Error")

    def post(self, request):
        name = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        user = Profile.objects.create(
            username=name,
            email=email,
            is_active=False
        )
        user.activate_code=hashlib.md5(name.encode("utf-8")).hexdigest()
        user.set_password(password)
        user.save()

        message = f"""
        Hello\n
        Please activate account: http://127.0.0.1:8000/api/activate/{user.activate_code}
        """
        send_mail(f"activation", message, "leader@rbssoft.by", ["wardag.as@gmail.com"])
        return Response("Success")

# Create your views here.
#http://127.0.0.1:8000/api/activate/b1b1f359c768446b15493abcbbea58b0
