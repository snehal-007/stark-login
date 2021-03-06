# Generated by Django 3.0.5 on 2020-06-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('signin_id', models.AutoField(primary_key=True, serialize=False)),
                ('u_name', models.CharField(max_length=50)),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('address_1', models.CharField(max_length=300)),
                ('address_2', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(default='', upload_to='home/images')),
            ],
        ),
    ]
