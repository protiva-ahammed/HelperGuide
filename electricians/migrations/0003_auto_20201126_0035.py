# Generated by Django 3.1.3 on 2020-11-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electricians', '0002_auto_20201126_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electrician',
            name='skill',
            field=models.CharField(max_length=50),
        ),
    ]
