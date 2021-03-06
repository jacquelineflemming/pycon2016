# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 22:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Preparation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('prep_time', models.IntegerField(help_text='in minutes')),
                ('cook_time', models.IntegerField(help_text='in minutes')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=6)),
                ('measurement', models.CharField(choices=[('tsp', 'teaspoon'), ('tbps', 'tablespoon'), ('c', 'cup'), ('gal', 'gallon'), ('quart', 'quart'), ('pint', 'pint'), ('g', 'gram'), ('mg', 'milligram'), ('kg', 'kilogram'), ('oz', 'ounce'), ('pinch', 'pinch')], max_length=10)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipies', to='meals.Ingredient')),
                ('preparation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='meals.Preparation')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='meals.Recipe')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='recipeingredient',
            unique_together=set([('recipe', 'ingredient', 'preparation')]),
        ),
    ]
