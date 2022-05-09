# Generated by Django 4.0.4 on 2022-04-30 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_delete_auditlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('eventName', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('actionType', models.CharField(max_length=100)),
                ('eventSpecificFields', models.JSONField(null=True)),
            ],
        ),
    ]
