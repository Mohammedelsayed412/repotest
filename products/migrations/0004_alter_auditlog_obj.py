# Generated by Django 4.0.4 on 2022-04-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auditlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditlog',
            name='obj',
            field=models.JSONField(null=True),
        ),
    ]
