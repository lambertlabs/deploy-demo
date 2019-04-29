from django.shortcuts import render

from .forms import WordForm


def homepage(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
    form = WordForm()
    return render(request, 'home.html', context={'form': form})
