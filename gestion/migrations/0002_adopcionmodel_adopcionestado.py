# Generated by Django 3.2.7 on 2021-10-15 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adopcionmodel',
            name='adopcionEstado',
            field=models.BooleanField(db_column='estado', default=True),
        ),
    ]