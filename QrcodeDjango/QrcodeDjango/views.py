from django.shortcuts import redirect,render

def redirect_form(request):
    return redirect('/homeapp/form')
