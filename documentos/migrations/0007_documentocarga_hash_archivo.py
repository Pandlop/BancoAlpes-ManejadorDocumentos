# Generated by Django 4.2.11 on 2024-05-11 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0006_remove_documentocarga_hash_archivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentocarga',
            name='hash_archivo',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
