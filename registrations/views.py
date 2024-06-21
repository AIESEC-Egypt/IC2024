from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponseBadRequest
from django.contrib.auth import login, authenticate
from .user_activation import *


def thankYou(request):
    return render(request, 'pages/thankYou_register.html')


def register(request):
    if request.method == 'POST':
        form = DelegateForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = User.objects.create_user(
                username=request.POST.get('new_username'), 
                password=request.POST.get('new_password1'),
                email=request.POST.get('aiesec_email'),
                is_active=True,
            )
            instance.save()
            form.save_m2m()
            user = authenticate(request, username=request.POST.get('new_username'), password=request.POST.get('new_password1'))
            login(request, user)
            return redirect('thankyou_view')
        else:
            errors = form.errors
            print(errors)

    else:
        form = DelegateForm()

    form.label_suffix = ''  
    return render(request, 'pages/register.html', {'form': form})

def checkIn(request):
    if request.method == 'POST':
        form = CheckInForm(request.POST, request.FILES)
        if form.is_valid():
            delegate = Delegate.objects.get(user=request.user)
            # print(delegate)
            delegate.name_as_per_passport = form.cleaned_data['name_as_per_passport']
            delegate.natonality = form.cleaned_data['natonality']
            delegate.current_living_country_territory = form.cleaned_data['current_living_country_territory']
            delegate.passport_scanned_photo = form.cleaned_data['passport_scanned_photo']
            delegate.passport_issue_date = form.cleaned_data['passport_issue_date']
            delegate.passport_expiry_date = form.cleaned_data['passport_expiry_date']
            delegate.room_preference = form.cleaned_data['room_preference']
            delegate.food.set(form.cleaned_data['food']) 
            delegate.allergies = form.cleaned_data['allergies']
            delegate.pre_and_post_trips = form.cleaned_data['pre_and_post_trips']
            delegate.merchandise = form.cleaned_data['merchandise']
            delegate.egyptian_nights_expectations = form.cleaned_data['egyptian_nights_expectations']
            delegate.cc_team_expecations = form.cleaned_data['cc_team_expecations']
            delegate.logistical_expectations = form.cleaned_data['logistical_expectations']
            delegate.agenda_expectations =form.cleaned_data['agenda_expectations']
            delegate.visa_support = form.cleaned_data['visa_support']
            delegate.save()
            return redirect('thankyou_view')
        else:
            errors = form.errors
            print(errors)

    else:
        form = CheckInForm()

    form.label_suffix = ''  
    return render(request, 'pages/checkin.html', {'form': form})


def setup_account_view(request, token, uidb64):
  User = get_user_model()
  try:
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)
    error = None
    if default_token_generator.check_token(user, token):
      if request.method == 'POST':
        form = CustomPasswordChangeForm(request.POST)
        if form.is_valid():
          user.username = request.POST.get('username')
          user.set_password(request.POST.get('new_password1'))
          user.is_active = True
          user.save()
          user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('new_password1'))
          login(request, user)
          return render(request, 'pages/index.html')
      else:
        form = CustomPasswordChangeForm()

        if form.errors:
          error = form.errors.get('__all__')
      return render(request, 'password_change.html', {'form': form, 'error': error})

    else:
      return HttpResponseBadRequest("Invalid token or user", content_type="text/plain")
  except (TypeError, ValueError, OverflowError, User.DoesNotExist):
      return HttpResponseBadRequest("Invalid request", content_type="text/plain")

