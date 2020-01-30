from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# home view
class Home(View):
    data = {}

    def get(self, request):
        return render(request, 'home.html', self.data)

    def post(self, request):
        pass

# about view
class About(View):
    data = {
        'title': 'About',
    }

    def get(self, request):
        return render(request, 'about.html', self.data)

    def post(self, request):
        pass
