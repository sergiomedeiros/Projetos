# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=50)),
                ('diretor', models.CharField(max_length=100)),
                ('elenco', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('nacionalidade', models.CharField(max_length=30)),
                ('datalancamento', models.DateField()),
                ('sinopse', models.CharField(max_length=200)),
                ('distribuidor', models.CharField(max_length=30)),
            ],
        ),
    ]
