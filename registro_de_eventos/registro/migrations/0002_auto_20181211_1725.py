# Generated by Django 2.1.4 on 2018-12-11 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='pub_date',
            new_name='fecha',
        ),
    ]
