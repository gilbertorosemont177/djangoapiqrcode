# Generated by Django 2.1.3 on 2018-12-04 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0003_auto_20181204_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulaire',
            name='img',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]