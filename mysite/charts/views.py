from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='/login')
def chart01(request):    
    return render(request, 'charts/chart01.html')
