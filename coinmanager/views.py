from django.shortcuts import render, redirect
from .models import Coin
from django.shortcuts import render, get_object_or_404
from .forms import CoinForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'coinmanager/index.html', {})

@login_required
def coins_list(request):
    coins = Coin.objects.all().order_by('value')
    return render(request, 'coinmanager/coin_list.html', {'coins':coins})

@login_required
def coin_detail(request, pk):
    coin = get_object_or_404(Coin, pk=pk)
    return render(request, 'coinmanager/coin_detail.html', {'coin': coin})

@login_required
def coin_new(request):
    if request.method == "POST":
        form = CoinForm(request.POST)
        if form.is_valid():
            coin = form.save(commit=False)
            coin.author = request.user
            coin.save()
            return redirect('coin_detail', pk=coin.pk)
    else:
        form = CoinForm()
    return render(request, 'coinmanager/coin_edit.html', {'form': form})

@login_required
def coin_edit(request, pk):
    coin = get_object_or_404(Coin, pk=pk)
    if request.method == "POST":
        form = CoinForm(request.POST, instance=coin)
        if form.is_valid():
            coin = form.save(commit=False)
            coin.author = request.user
            coin.save()
            return redirect('coin_detail', pk=coin.pk)
    else:
        form = CoinForm(instance=coin)
    return render(request, 'coinmanager/coin_edit.html', {'form': form})