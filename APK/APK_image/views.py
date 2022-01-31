from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from APK_image.models import Violation, GasPipelines
from APK_image.forms import ViolationForm


class Index(ListView):
    model = Violation
    template_name = 'APK_image/index.html'
    context_object_name = 'violations'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gaz_pipelines'] = GasPipelines.objects.all()
        context['title'] = 'Главная страница'
        return context

# def index(request):
#     gaz_pipelines = GasPipelines.objects.all()
#     violations = Violation.objects.all()
#     context = {'violations': violations,
#                'gaz_pipelines': gaz_pipelines,
#                }
#     return render(request=request, template_name='APK_image/index.html', context=context)


class Filter_Violations(ListView):
    model = Violation
    template_name = 'APK_image/index.html'
    context_object_name = 'violations'
    allow_empty = False

    def get_queryset(self):
        return Violation.objects.filter(gas_pipeline__pk=self.kwargs['gas_pipeline_pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gaz_pipelines'] = GasPipelines.objects.all()
        context['title'] = str(context['violations'][0].gas_pipeline)
        context['gas_pipeline_selected'] = context['violations'][0].gas_pipeline_id
        return context


# def filter_violations(request, gas_pipeline_pk):
#     violations = Violation.objects.filter(gas_pipeline=gas_pipeline_pk)
#     gaz_pipelines = GasPipelines.objects.all()
#     context = {'violations': violations,
#                'gaz_pipelines': gaz_pipelines,
#                }
#     return render(request=request, template_name='APK_image/index.html', context=context)


# def register(request):
#     form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

class ViolationFormView(CreateView):
    form_class = ViolationForm
    template_name = 'APK_image/add_violation.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gaz_pipelines'] = GasPipelines.objects.all()
        context['title'] = 'Добавить замечание'
        return context


