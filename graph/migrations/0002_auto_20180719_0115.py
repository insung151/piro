# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-07-18 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='git_user_name',
            new_name='github_username',
        ),
    ]
