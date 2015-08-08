# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=14)),
            ],
        ),
    ]
