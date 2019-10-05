# Generated by Django 3.0a1 on 2019-10-14 19:47

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good_flow_app', '0037_drop_gin_index_with_condition'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='testtable',
            index=django.contrib.postgres.indexes.GistIndex(fields=['test_field_tsv'], name='test_index'),
        ),
    ]
