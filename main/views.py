from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreForm


def index(request):
    stores = Store.objects.all()
    return render(request, 'main/index.html', {'title': 'Main Page', 'stores': stores})


def admin(request):
    return render(request, 'admin')


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form was wrong'

    form = StoreForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

def basket(request):
    return render(request, 'main/basket.html')