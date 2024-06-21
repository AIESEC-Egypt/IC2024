from django.shortcuts import render, redirect
from .forms import *



def thankYou_partner(request):
    return render(request, 'pages/thankYou_partner.html')

def partner(request):
    if request.method == 'POST':
        form = PartnersForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('thankYou_partner_view')
        else:
            errors = form.errors
            print(errors)

    else:
        form = PartnersForm()

    form.label_suffix = ''  
    return render(request, 'pages/partners.html', {'form': form})  