# Generated by Django 3.0.5 on 2020-06-08 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200608_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
