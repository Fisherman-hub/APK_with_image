from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'': ''}

    return render(request=request, template_name='APK_image/index.html', context=context)
