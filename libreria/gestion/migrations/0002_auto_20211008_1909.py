# Generated by Django 3.2.7 on 2021-10-09 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('gestion', '0001_creaciontablasfinal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientemodel',
            name='perfilCliente',
        ),
        migrations.RemoveField(
            model_name='clientemodel',
            name='perfiles',
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='clienteApellido',
            field=models.CharField(db_column='apellido', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='clienteCorreo',
            field=models.EmailField(db_column='email', default='', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='clientePassword',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='clienteTipo',
            field=models.IntegerField(choices=[(1, 'ADMINISTRADOR'), (2, 'COLABORADOR'), (3, 'CLIENTE')], db_column='tipo', default=3),
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='password',
            field=models.CharField(default='', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='clientemodel',
            name='clienteNombre',
            field=models.CharField(db_column='nombre', max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='PerfilModel',
        ),
    ]