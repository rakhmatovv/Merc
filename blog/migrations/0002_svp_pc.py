# Generated by Django 4.2 on 2023-08-10 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='svp',
            name='pc',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
