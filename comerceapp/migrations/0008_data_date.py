# Generated by Django 4.2.7 on 2023-11-20 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comerceapp', '0007_alter_data_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='date',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
