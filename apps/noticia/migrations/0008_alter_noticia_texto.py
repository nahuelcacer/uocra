# Generated by Django 4.0.6 on 2022-08-27 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0007_alter_noticia_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='texto',
            field=models.TextField(null=True),
        ),
    ]