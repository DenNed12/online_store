# Generated by Django 4.2.7 on 2023-12-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='added_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
