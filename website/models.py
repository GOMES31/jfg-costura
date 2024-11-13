import os
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Partner(models.Model):
    name = models.CharField('Nome', max_length=100, blank=False, null=False)
    order = models.IntegerField('Ordem', unique=True, )
    active = models.BooleanField('Ativo', default=True)
    image = models.ImageField('Imagem', upload_to='marquee/', blank=False, null=False)

    class Meta:
        verbose_name = 'Parceiro'
        verbose_name_plural = 'Parceiros'

    # Self increment order number 
    def save(self, *args, **kwargs):
        if self.order is None:
            # Get the highest current order value and add 1
            max_order = Partner.objects.aggregate(models.Max('order'))['order__max'] or 0
            self.order = max_order + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Machine(models.Model):
    name = models.CharField('Nome', max_length=120, blank=False, null=False)
    order = models.IntegerField('Ordem', unique=True, )
    description = models.TextField('Descrição', max_length=250, blank=False, null=False)
    slug = models.SlugField("Slug", max_length=120, blank=True, editable=False, unique=True)

    class Meta:
        verbose_name = 'Máquina'  
        verbose_name_plural = 'Máquinas'

    # Self increment order number 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if self.order is None:
            # Get the highest current order value and add 1
            max_order = Machine.objects.aggregate(models.Max('order'))['order__max'] or 0
            self.order = max_order + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
def machine_image_upload_path(instance, filename):
    # Generate a slugified folder name based on the machine name
    folder_name = slugify(instance.machine.name)

    return os.path.join('machines', folder_name, filename)

class MachineImage(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name = 'images')
    image = models.ImageField(upload_to=machine_image_upload_path)

    def __str__(self):
        return f'Image for {self.machine.name}'
