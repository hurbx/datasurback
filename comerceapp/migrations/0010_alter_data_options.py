# Generated by Django 4.2.6 on 2023-11-21 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comerceapp', '0009_alter_data_dolar_obs_alter_data_euro_alter_data_uf_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'ordering': ['date'], 'verbose_name': 'Data', 'verbose_name_plural': 'Datas'},
        ),
    ]
