from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic import CreateView


from .forms import ProfileForm
from .models import Profile
# Create your views here.

class CreateProfileView(CreateView):

    template_name = 'profiles/create_profile.html'
    model=Profile
    fields = '__all__'
    success_url = 'profiles/create_profile.html'

    # can add form class if we want to customize form
    # form_class = ProfileForm
