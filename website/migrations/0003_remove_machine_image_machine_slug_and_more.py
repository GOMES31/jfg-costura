# Generated by Django 5.1.3 on 2024-11-13 14:26

import django.db.models.deletion
import website.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_machine_alter_partner_options_alter_partner_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='image',
        ),
        migrations.AddField(
            model_name='machine',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=120, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=models.ImageField(upload_to='marquee/', verbose_name='Imagem'),
        ),
        migrations.CreateModel(
            name='MachineImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=website.models.machine_image_upload_path)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='website.machine')),
            ],
        ),
    ]
