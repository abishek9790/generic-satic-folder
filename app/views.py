from django.shortcuts import render

# Create your views here.
def statices(request):
    return render(request, 'statices.html')
