# Generated by Django 2.2.16 on 2020-09-23 18:08

from django.db import migrations
import django_jsonfield_backport.models


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0023_auto_20200916_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preview',
            name='sizes',
            field=django_jsonfield_backport.models.JSONField(default=dict),
        ),
    ]
