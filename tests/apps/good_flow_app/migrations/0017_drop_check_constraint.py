# Generated by Django 3.1 on 2019-09-22 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good_flow_app', '0016_add_check_constraint'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='testtable',
            name='test_check_constraint',
        ),
    ]
