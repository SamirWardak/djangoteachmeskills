import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import HttpResponseRedirect

from .models import News
from customer.models import Profile
from .forms import NameForm, RegistrationForm, ImageForm

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
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data.get("image")
            name = form.cleaned_data.get("name")
            News.objects.create(name=name, create_date="2020-02-02", image=img, file=img)
            return HttpResponse("Ok", content_type="text/plain")
        return HttpResponse("error", content_type="text/plain")



