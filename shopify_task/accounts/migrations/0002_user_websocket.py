# Generated by Django 4.2.1 on 2023-06-02 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='websocket',
            field=models.TextField(blank=True, null=True),
        ),
    ]
