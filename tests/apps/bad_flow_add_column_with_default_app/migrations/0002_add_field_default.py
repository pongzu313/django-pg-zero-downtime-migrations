# Generated by Django 3.1 on 2019-09-22 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bad_flow_add_column_with_default_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtable',
            name='field',
            field=models.IntegerField(default=0),
        ),
    ]
