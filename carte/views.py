from django.shortcuts import render

# Create your views here.
def card_list(request):
    return render(request, 'carte/carte_list.html', {})
