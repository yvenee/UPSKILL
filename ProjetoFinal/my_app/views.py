from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home Page!")

def soma(resquest, num1, num2):
    soma = num1 + num2
    return HttpResponse("<h1>A soma de {} e {}, é igual a: {}</h1>" .format(num1, num2, soma))