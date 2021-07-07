import django
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.

# def storeFile(file):
#     with open("temp/1.jpg" , "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

# when using CreateView we don't need this much line of code

# class CreateProfileView(View): 
    def get(self, request):
        form = ProfileForm()
        return render(request , "profiles/create_profile.html", {
            "form": form
        })


    def post(self , request):
        submitted_form = ProfileForm(request.POST , request.FILES)
        if(submitted_form.is_valid()) : 
            # storeFile(request.FILES['image'])
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            return HttpResponseRedirect("/profiles")

        return render(request , "profiles/create_profile.html", {
            "form": submitted_form
        })

class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profile.html"
    context_object_name = "profiles"

