# Generated by Django 4.0.6 on 2022-08-16 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentario', '0002_alter_comentario_options_comentario_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='comentario',
            new_name='texto',
        ),
    ]
