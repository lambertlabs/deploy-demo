from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import WordForm
from .models import Word


def homepage(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
    form = WordForm()
    return render(request, 'home.html', context={'form': form, 'words': Word.objects.all()})
