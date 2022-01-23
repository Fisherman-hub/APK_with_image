from django.http import HttpResponse
from django.shortcuts import render
from APK_image.models import Violation, GasPipelines


def index(request):
    gaz_pipelines = GasPipelines.objects.all()
    violations = Violation.objects.all()
    context = {'violations': violations,
               'gaz_pipelines': gaz_pipelines,
               }
    return render(request=request, template_name='APK_image/index.html', context=context)


def filter_violations(request, gas_pipeline_pk):
    violations = Violation.objects.filter(gas_pipeline=gas_pipeline_pk)
    gaz_pipelines = GasPipelines.objects.all()
    context = {'violations': violations,
               'gaz_pipelines': gaz_pipelines,
               }
    return render(request=request, template_name='APK_image/index.html', context=context)