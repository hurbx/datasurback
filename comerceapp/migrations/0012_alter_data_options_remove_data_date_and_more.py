# Generated by Django 4.2.6 on 2023-12-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comerceapp', '0011_alter_data_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'verbose_name': 'Data', 'verbose_name_plural': 'Datas'},
        ),
        migrations.RemoveField(
            model_name='data',
            name='date',
        ),
        migrations.RemoveField(
            model_name='data',
            name='dolar_obs',
        ),
        migrations.RemoveField(
            model_name='data',
            name='euro',
        ),
        migrations.RemoveField(
            model_name='data',
            name='uf',
        ),
        migrations.RemoveField(
            model_name='data',
            name='utm',
        ),
        migrations.AddField(
            model_name='data',
            name='day',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='data',
            name='month',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='data',
            name='value',
            field=models.CharField(default='', max_length=10),
        ),
    ]