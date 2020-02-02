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
        self.context['form'] = UserRegisterForm(request.POST or None)

        if self.context['form'].is_valid():
            # insert
            self.context['form'].save()

            username = self.context['form'].cleaned_data.get('username')

            # set flash message
            messages.success(request, f'Account created for {username}!')

            # redirect
            return redirect('blog.home')

        # view
        return render(request, 'register.html', self.context)

