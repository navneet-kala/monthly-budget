# Generated by Django 3.1.7 on 2021-03-13 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0009_auto_20210313_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthlysummary',
            name='expense_date',
        ),
    ]
