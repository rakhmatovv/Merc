# Generated by Django 4.2 on 2023-08-18 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_avto_avto_year_remove_avto_clas_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zakaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(max_length=50)),
                ('carname', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='cars',
            name='pc',
        ),
    ]
