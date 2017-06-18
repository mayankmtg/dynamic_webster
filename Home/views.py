from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Details
from django.db.models import Q
import operator


def index(request):
	heading=Details.objects.filter(title='Heading')
	Copyright=Details.objects.filter(title='Copyright')
	detail4=Details.objects.filter(title='detail4')
	detail3=Details.objects.filter(title='detail3')
	detail2=Details.objects.filter(title='detail2')
	detail1=Details.objects.filter(title='detail1')
	subheading2=Details.objects.filter(title='subheading2')
	subheading1=Details.objects.filter(title='subheading1')

	context={
		'heading': heading,
		'Copyright': Copyright,
		'detail4': detail4,
		'detail3': detail3,
		'detail2': detail2,
		'detail1': detail1,
		'subheading2': subheading2,
		'subheading1': subheading1,
		
	}
	return render(request, 'Home/index.html', context)

