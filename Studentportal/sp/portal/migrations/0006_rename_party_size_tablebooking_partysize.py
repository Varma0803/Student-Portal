# Generated by Django 5.0.1 on 2024-02-19 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_remove_tablebooking_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablebooking',
            old_name='party_size',
            new_name='partysize',
        ),
    ]