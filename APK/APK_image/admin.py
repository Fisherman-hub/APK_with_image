from django.contrib import admin
from APK_image.models import Violation, GasPipelines


class ViolationAdmin(admin.ModelAdmin):
    list_display = ['object', 'gas_pipeline', 'date_created', 'date_elimination']
    list_filter = ('object', 'gas_pipeline', 'date_created', 'date_elimination')
    fields = ['object', 'gas_pipeline']


class GasPipelinesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Violation, ViolationAdmin)
admin.site.register(GasPipelines, GasPipelinesAdmin)
