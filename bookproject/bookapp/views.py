from django.shortcuts import render

def cover(request):
    return render(request, 'bookcover.html')
