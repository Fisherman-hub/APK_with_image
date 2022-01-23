from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class GasPipelines(models.Model):
    gas_pipeline = models.CharField(max_length=200)

    def __str__(self):
        return self.gas_pipeline


    class Meta:
        verbose_name = 'Газопровод-отвод'
        verbose_name_plural = 'Газопроводы-отводы'


class Violation(models.Model):
    photo_violation = models.ImageField(upload_to='photo_violation/%Y-%m-%d', verbose_name='Фото замечания')
    photo_violation_phumbnail = ImageSpecField(source='photo_violation',
                                               processors=[ResizeToFit(300, 300)],
                                               options={'quality': 60})
    photo_with_out_violation = models.ImageField(blank=True, verbose_name='Фото устранения замечания')
    object = models.CharField(max_length=255, verbose_name='Объект')
    text_violation = models.TextField(verbose_name='Описание нарушения')
    date_created = models.DateField(auto_now=True)
    date_elimination = models.DateField(verbose_name='Дата устранения')
    gas_pipeline = models.ForeignKey(GasPipelines, on_delete=models.PROTECT, verbose_name='Газопровод-отвод')



    class Meta:
        verbose_name = 'Замечание'
        verbose_name_plural = 'Замечания'
        ordering = ['date_elimination']

    def __str__(self):
        return '{} {}'.format(self.object, self.gas_pipeline)