# Generated by Django 3.0.5 on 2020-06-07 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200607_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]