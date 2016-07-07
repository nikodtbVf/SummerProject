# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlimage', models.TextField()),
                ('hand', models.CharField(max_length=20)),
                ('finger', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('work', models.TextField()),
                ('cellphone', models.CharField(max_length=12)),
                ('street', models.CharField(max_length=50)),
                ('number_house', models.IntegerField()),
                ('colony', models.CharField(max_length=50)),
                ('postalcode', models.IntegerField()),
                ('municipality', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_detector.Person'),
        ),
    ]
