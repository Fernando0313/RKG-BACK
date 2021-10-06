# Generated by Django 3.2.7 on 2021-10-06 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CabeceraModel',
            fields=[
                ('cabeceraId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('cabeceraFecha', models.DateTimeField(auto_now_add=True, db_column='fecha')),
                ('cabeceraTipo', models.TextField(choices=[('V', 'VENTA'), ('C', 'COMPRA')], db_column='tipo')),
            ],
            options={
                'verbose_name': 'cabecera',
                'verbose_name_plural': 'cabeceras',
                'db_table': 'cabecera_operaciones',
            },
        ),
        migrations.CreateModel(
            name='PerfilModel',
            fields=[
                ('perfilId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('perfilNick', models.CharField(db_column='nick', max_length=19)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoModel',
            fields=[
                ('productoId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('productoNombre', models.CharField(db_column='nombre', max_length=50, verbose_name='nombre')),
                ('productoPrecio', models.DecimalField(db_column='precio', decimal_places=2, max_digits=5, verbose_name='precio')),
                ('productoDescripcion', models.CharField(db_column='descripcion', max_length=100, verbose_name='descripcion')),
                ('productoFoto', models.ImageField(db_column='foto', null=True, upload_to='productos/')),
                ('productoCantidad', models.IntegerField(db_column='cantidad', default=0)),
                ('updatedAt', models.DateTimeField(auto_now=True, db_column='updated_at')),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
                'db_table': 'productos',
                'ordering': ['-productoPrecio'],
            },
        ),
        migrations.CreateModel(
            name='DetalleModel',
            fields=[
                ('detalleId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('detalleCantidad', models.IntegerField(db_column='cantidad')),
                ('detalleImporte', models.DecimalField(db_column='importe', decimal_places=2, max_digits=5)),
                ('cabeceras', models.ForeignKey(db_column='cabecera_operaciones_id', on_delete=django.db.models.deletion.PROTECT, related_name='cabeceraDetalles', to='gestion.cabeceramodel')),
                ('productos', models.ForeignKey(db_column='productos_id', on_delete=django.db.models.deletion.PROTECT, related_name='productoDetalles', to='gestion.productomodel')),
            ],
            options={
                'verbose_name': 'detalle',
                'verbose_name_plural': 'detalles',
                'db_table': 'detalle_operaciones',
            },
        ),
        migrations.CreateModel(
            name='ClienteModel',
            fields=[
                ('clienteId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('clienteNombre', models.CharField(db_column='nombre', max_length=19)),
                ('clienteDocumento', models.CharField(db_column='documento', max_length=8)),
                ('clienteCelular', models.IntegerField(db_column='celular', null=True, unique=True)),
                ('perfilCliente', models.CharField(db_column='PerfilModel', max_length=19)),
                ('perfiles', models.ForeignKey(db_column='perfiles_id', on_delete=django.db.models.deletion.PROTECT, related_name='perfilCliente0', to='gestion.perfilmodel')),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
                'db_table': 'clientes',
            },
        ),
        migrations.AddField(
            model_name='cabeceramodel',
            name='clientes',
            field=models.ForeignKey(db_column='clientes_id', on_delete=django.db.models.deletion.PROTECT, related_name='clienteCabeceras', to='gestion.clientemodel'),
        ),
        migrations.CreateModel(
            name='AdopcionModel',
            fields=[
                ('adopcionId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('adopcionNombre', models.CharField(db_column='nombre', max_length=14)),
                ('adopcionEdad', models.IntegerField(db_column='edad', null=True, unique=True)),
                ('adopcionTamaño', models.TextField(choices=[('P', 'PEQUEÑO'), ('M', 'MEDIANO'), ('G', 'GRANDE')], db_column='tamaño', default='M')),
                ('adopcionCaracteristicas', models.CharField(db_column='caracteristicas', max_length=100)),
                ('clientes', models.OneToOneField(db_column='cliente_id', on_delete=django.db.models.deletion.CASCADE, related_name='clienteAdopcion', to='gestion.clientemodel')),
            ],
            options={
                'verbose_name': 'adopcion',
                'verbose_name_plural': 'adopciones',
                'db_table': 'adopciones',
                'ordering': ['-adopcionTamaño'],
            },
        ),
    ]
