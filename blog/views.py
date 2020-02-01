from django.shortcuts import render
from django.views import View
from .models import Post

# home view
class Home(View):
    context = {
        'posts': Post.objects.all(),
    }

    def get(self, request):
        return render(request, 'home.html', self.context)

    def post(self, request):
        pass

# about view
class About(View):
    context = {
        'title': 'About',
    }

    def get(self, request):
        return render(request, 'about.html', self.context)

    def post(self, request):
        pass
