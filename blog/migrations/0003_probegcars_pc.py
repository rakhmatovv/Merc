# Generated by Django 4.2 on 2023-08-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_svp_pc'),
    ]

    operations = [
        migrations.AddField(
            model_name='probegcars',
            name='pc',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
