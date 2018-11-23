from django.shortcuts import redirect

def redirect_form(request):
    return redirect('/homeapp/form')