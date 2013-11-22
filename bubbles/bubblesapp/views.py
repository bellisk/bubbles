from django.shortcuts import render
from bubbles.bubblesapp.auth import *
from django.shortcuts import get_object_or_404 as go4
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm

def frontpage(request):
    if logged_in(request):
        return bubbles(request)
    if request.method == 'POST':
        user = authenticate(request.POST['username'], request.POST['password'])
        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('bubbles.bubblesapp.views.frontpage'))
        else:
            return render(request, 'frontpage.html', {'username': request.POST['username'], 'error': 'Account not found or incorrect password.'})
    else:
        return render(request, 'frontpage.html')

@require_login
def bubbles(request):
    return render(request, 'bubbles.html', {'profile': profile(request)})

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'last_contact', 'frequency']

@require_login
def edit_contact(request, contact_id):
    if contact_id == 'create':
        contact = Contact(profile=profile(request))
    else:
        contact = go4(Contact, id=contact_id, profile=profile(request))
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('bubbles.bubblesapp.views.frontpage'))
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit_contact.html', {'form': form})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['reminder_interval', 'reminder_threshold']

@require_login
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile(request))
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=profile(request))
    return render(request, 'edit_profile.html', {'form': form})
