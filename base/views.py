from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import Gameform


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('game-list')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Este usuário não existe!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Nome de usuário ou senha estão incorretos!')



    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutPage(request):
    logout(request)

    return redirect('/')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('game-list')
        else:
            messages.error(request, 'Ocorreu um erro durante o processo. Tente novamente!')

    context = {'form': form}
    return render(request, 'base/login_register.html', context)

def gameList(request):
    games = Game.objects.all()

    context = {'games':games}
    return render(request, 'base/game_list.html', context)


@login_required(login_url='login')
def createGame(request):
    form = Gameform()

    if request.method == 'POST':
        form = Gameform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'base/create_game.html', context)


@login_required(login_url='login')
def updateGame(request, pk):
    game = Game.objects.get(id=pk)
    form = Gameform(instance=game)

    if request.method == 'POST':
        form = Gameform(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('/')

        
    context = {'game':game, 'form':form}
    return render(request, 'base/create_game.html', context)

@login_required(login_url='login')
def deleteGame(request, pk):
    game = Game.objects.get(id=pk)

    if request.method == 'POST':
        game.delete()
        return redirect('/')

    context = {'game':game}
    return render(request, 'base/delete_game.html', context)

def detalheGame(request, pk):
    game = Game.objects.get(id=pk)

    context = {'game': game}
    return render(request, 'base/detalhe_game.html', context)
