# Generated by Django 3.0.5 on 2021-01-15 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('title_api', '0011_auto_20210115_2213'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('id', 'author'), name='unique_review'),
        ),
    ]
