from django.shortcuts import render

def _main(request):
    return render(request, 'edu/main.html')