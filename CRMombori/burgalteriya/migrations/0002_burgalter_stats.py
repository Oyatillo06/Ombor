# Generated by Django 4.0.1 on 2022-01-16 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statistika', '0001_initial'),
        ('burgalteriya', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='burgalter',
            name='stats',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='statistika.stats'),
        ),
    ]
