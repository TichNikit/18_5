from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserRegister

# Create your views here.

users = ['user1', 'user2', 'user3', 'user4']


def main(request):
    return render(request, 'welcom.html')

def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        if password == repeat_password and age >= 18 and username not in users:
            return HttpResponse(f'Приветствуем, {username}')
        elif username in users:
            return HttpResponse('Пользователь уже существует')
        elif password != repeat_password:
            return HttpResponse('Пароли не совпадают')
        elif age < 18:
            return HttpResponse('Вы должны быть старше 18')
        else:
            return HttpResponse('Что-то невообразимое')
    return render(request, 'registration_page.html')


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and age >= 18 and username not in users:
                info['message'] = f'Приветствуем, {username}!'
                return render(request, 'registration_page.html', info)
            elif username in users:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', info)
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', info)
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', info)
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'registration_page.html', info)



