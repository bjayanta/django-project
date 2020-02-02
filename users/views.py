from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import UserRegisterForm

class Register(View):
    context = {
        'title': 'Register',
    }

    def get(self, request):
        self.context['form'] = UserRegisterForm()
        return render(request, 'register.html', self.context)

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            # insert
            form.save()

            username = form.cleaned_data.get('username')

            # set flash message
            messages.success(request, f'Account created for {username}!')

            return redirect('blog.home')
        else:
            self.context['form'] = UserRegisterForm()
            return render(request, 'register.html', self.context)

