# Generated by Django 3.1.1 on 2020-09-05 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0002_auto_20200905_1809'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goal',
            options={'ordering': ['-name']},
        ),
    ]