# Generated by Django 3.1 on 2020-09-05 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvals',
            name='married',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=15),
        ),
    ]
