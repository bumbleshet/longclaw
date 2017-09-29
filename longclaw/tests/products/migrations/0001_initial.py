# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', wagtail.wagtailcore.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProductIndex',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('ref', models.CharField(max_length=32)),
                ('stock', models.IntegerField(default=0)),
                ('description', wagtail.wagtailcore.fields.RichTextField()),
                ('product', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='products.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
