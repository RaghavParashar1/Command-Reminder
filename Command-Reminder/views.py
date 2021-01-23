from django.views.generic import ListView

from .models import ccmdr

class HomePageView(ListView):
	model = ccmdr
	template_name = 'home.html'
