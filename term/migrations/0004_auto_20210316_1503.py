# Generated by Django 3.1.7 on 2021-03-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('term', '0003_term_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='term/images'),
        ),
    ]