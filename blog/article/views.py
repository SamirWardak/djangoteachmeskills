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

from .models import News
from customer.models import Profile
from .forms import NameForm, RegistrationForm, ImageForm
from .serializer import NewsSerializer, ContactFormSerializer


class NewsView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        context['News'] = News.objects.all()
        return context


class GetView(View):
    template_name = 'index1.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': 1})

    def post(self):
        pass

    def put(self):
        pass

    def pach(self):
        pass


class BootStrapView(View):
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        gallery = News.objects.all()
        search = News.objects.filter(name__icontains="asdasd").all()
        for i in search:
            print(i)
        return render(request, self.template_name, {'gallery': gallery})


class get_name(View):
    template_name = 'name.html'

    def get(self, request, *args, **kwargs):
        form = NameForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse("Ok", content_type='text/plain')
        else:
            return HttpResponse("error", content_type='text/plain')


class RegistrationView(View):
    template_name = 'registration.html'

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        data = request.POST
        user = data["user_name"]
        email = data["email_id"]
        password = data["password"]
        password_retype = data["password_retype"]
        if form.is_valid():
            if Profile.objects.filter(username=user).exists() is False and password == password_retype:
                profile = Profile.objects.create(username=user, email=email, is_active=False)
                profile.set_password(password)
                profile.save()
                return HttpResponse("Ok", content_type="text/plain")
        return HttpResponse("error", content_type="text/plain")


class ImageView(View):
    template_name = 'image.html'

    def get(self, request):
        form = ImageForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        data = request.POST
        if form.is_valid():
            print("Ok")
            return HttpResponse("Ok", content_type="text/plain")
        return HttpResponse("error", content_type="text/plain")


class ContactFormView(GenericAPIView):
    serializer_class = ContactFormSerializer

    queryset = ''

    def post(self, request):
        name = request.data.get("name")
        email = request.data.get("email")
        message = request.data.get("message")
        sender = "wardag.as@gmail.com"
        send_mail(f"Test email from {name}", message, sender, [sender, email])
        return Response("Good")


class NewsRestView(GenericAPIView):
    serializer_class = NewsSerializer

    queryset = News.objects.all()

    def get(self, request):
        news = News.objects.all()
        serializer = self.serializer_class(news, many=True)
        return Response(serializer.data)

    def post(self, request):
        News.objects.create(
            name=request.data.get("name"),
            create_date=request.data.get("create_date"),
            image=request.data.get("image"),
            file=request.data.get("file")
            # activate_code=()
        )
        # send_mail(f"Test email from {name}", message, sender, [sender, email])
        return Response("Success")


# class NewsSingleRestView(RetrieveUpdateDestroyAPIView):
class NewsSingleRestView(GenericAPIView):
    serializer_class = NewsSerializer
    lookup_field = 'id'
    queryset = News.objects.all()

    def get(self, request, id):
        news = News.objects.get(id=id)
        serializer = self.serializer_class(news, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        news = News.objects.get(id=id)
        news.name = request.data.get("name")
        news.create_date = request.data.get("create_date")
        news.image = request.data.get("image")
        news.file = request.data.get("file")
        news.save()
        return Response("Success")

    def delete(self, request, id):
        News.objects.get(id=id).delete()
        return Response("Success")
