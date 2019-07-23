from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    data = {'usuario': request.user}
    return render(request, 'core/index.html', data)
