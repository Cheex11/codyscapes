import os
from django.shortcuts import render

from rest_framework import generics

from .models import Photo
from . import models
from . import serializers
from . import forms

#For the email part:
from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


def index(request):
	photos = Photo.objects.all().filter(recent="true").order_by('-date')
	# photos = Photo.objects.all().filter(visible="true").filter(date__year=2018).order_by('-date')
	#photos = Photo.objects.all().filter(visible="true").order_by('-date')
	form = forms.SuggestionForm()
	if request.method == 'POST':
		form = forms.SuggestionForm(request.POST)
		if form.is_valid():
			#print("good form")
			data = request.POST.get('year')
			#return HttpResponseRedirect(reverse('suggest'))
			if data == "all":
				photos = Photo.objects.all().filter(visible="true").order_by('-date')
			elif data == "recent":
				photos = Photo.objects.all().filter(recent="true").order_by('-date')
			else:
				photos = Photo.objects.all().filter(visible="true").filter(date__year=data).order_by('-date')
			return render(request, 'photos/index.html', {'photos': photos, 'key': os.environ['MAPS_KEY'], 'form': form})
	return render(request, 'photos/index.html', {'photos': photos, 'key': os.environ['MAPS_KEY'], 'form': form})

def dev_form(request):
	form = forms.SuggestionForm()
	return render(request, 'photos/index2.html', {'form': form})

def photo_details(request, slug):
	photo = get_object_or_404(Photo, slug=slug)
	try:
		next_photo = Photo.get_next_by_date(photo, visible=True)
	except:
		next_photo = Photo.objects.filter(visible=True).order_by('date')[0]
	try:
		prev_photo = Photo.get_previous_by_date(photo, visible=True)
	except:
		prev_photo = Photo.objects.filter(visible=True).order_by('-date')[0]
	return render(request, 'photos/details.html', {'photo': photo,'next_photo': next_photo,'prev_photo': prev_photo, 'key': os.environ['MAPS_KEY']})


def suggestion_view(request):
	form = forms.SuggestionForm()
	if request.method == 'POST':
		form = forms.SuggestionForm(request.POST)
		if form.is_valid():
			print("good form")
			#send_mail(
			#	'Email From {}'.format(form.cleaned_data['name']),
			#	form.cleaned_data['suggestion'],
			#	'{name} <{email}>'.format(**form.cleaned_data),
			#	['cheex11@gmail.com']
			#)
			#messages.add_message(request, messages.SUCCESS,
			#					'The year has changed')
			data = request.POST.get('year')
			print data
			#return HttpResponseRedirect(reverse('suggest'))
			photos = Photo.objects.all().filter(visible="true").filter(date__year=data).order_by('-date')
			return render(request, 'photos/index.html', {'photos': photos, 'key': os.environ['MAPS_KEY']})
	return render(request, 'photos/suggestion_form.html', {'form': form})


#API views
class ListCreatePhoto(generics.ListCreateAPIView):
	queryset = models.Photo.objects.all()
	serializer_class = serializers.PhotoSerializer

class RetrieveUpdateDestroyPhoto(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Photo.objects.all()
	serializer_class = serializers.PhotoSerializer
