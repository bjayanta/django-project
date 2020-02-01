from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# home view
class Home(View):
    context = {
        'posts': [
            {
                'author': 'Jayanta Biswas', 
                'title': 'Blog post 1', 
                'content': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 
                'date_posted': 'August 27, 2018'
            },
            {
                'author': 'Joy Khan', 
                'title': 'Blog post 2', 
                'content': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 
                'date_posted': 'August 28, 2018'
            },
            {
                'author': 
                'Shibbir Ahmad', 
                'title': 'Blog post 3', 
                'content': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 
                'date_posted': 'August 29, 2018'
            },
            {
                'author': 'Amor Chandra', 
                'title': 'Blog post 4', 
                'content': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 
                'date_posted': 'August 30, 2018'
            },
            {
                'author': 'Baky Billha', 
                'title': 'Blog post 5', 
                'content': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 
                'date_posted': 'August 31, 2018'
            },
        ]
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
