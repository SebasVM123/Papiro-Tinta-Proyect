# Generated by Django 4.2.5 on 2023-11-09 15:30

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('groups', models.ManyToManyField(related_name='clientes', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='clientes_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='tarjeta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=50)),
                ('codigo', models.IntegerField()),
                ('fecha_expiracion', models.DateField()),
                ('banco', models.CharField(max_length=50)),
                ('franquicia', models.CharField(max_length=50)),
                ('propietario', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='cliente_tarjeta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cliente')),
                ('id_tarjeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tarjeta')),
            ],
        ),
        migrations.CreateModel(
            name='cliente_categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categoria')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cliente')),
            ],
        ),
    ]
