# Generated by Django 4.0.6 on 2022-08-18 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Autoridades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250, null=True)),
                ('imagen', models.ImageField(blank=True, default='institucional/default.png', null=True, upload_to='institucional')),
                ('cargo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='institucional.cargo')),
            ],
        ),
    ]
