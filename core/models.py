from django.db import models
import json
from datetime import datetime
import requests

class ProductoJSON:
    def __init__(self, nombre, datos):
        self.nombre = nombre
        self.precio_coto = datos.get('coto')
        self.precio_dia = datos.get('dia')
        self.precio_jumbo = datos.get('jumbo')
        self.fecha_actualizacion = datetime.now()

    @staticmethod
    def all():
        # URL del Gist (deberás reemplazar esta URL con la tuya)
        url = "https://gist.githubusercontent.com/Walter-FB/f091d2a3a416cd73170aed0a52a0e9fd/raw/effc5ab3009663145c2298998d6dad640eda785f/productos.json"
        try:
            response = requests.get(url)
            data = response.json()
            
            # Extraer fecha de actualización si existe
            fecha_str = data.get('ultima_actualizacion')
            if fecha_str:
                try:
                    fecha_actualizacion = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
                except:
                    fecha_actualizacion = None
            else:
                fecha_actualizacion = None
            
            # Obtener productos (pueden estar en 'productos' o directamente en data)
            productos_data = data.get('productos', data)
            
            productos = []
            for nombre, datos in productos_data.items():
                # Saltar la clave 'ultima_actualizacion' si está en el nivel raíz
                if nombre == 'ultima_actualizacion':
                    continue
                producto = ProductoJSON(nombre, datos)
                # Sobrescribir la fecha si la obtuvimos del JSON
                if fecha_actualizacion:
                    producto.fecha_actualizacion = fecha_actualizacion
                productos.append(producto)
            return productos
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            return []

class Cafe(models.Model):
    nombre = models.CharField(primary_key=True, max_length=255)
    precio_coto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_dia = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_jumbo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'cafe'
        managed = False

    def __str__(self):
        return self.nombre

















# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
"""from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cafe(models.Model):
    nombre = models.CharField(unique=True, max_length=255)
    imagen = models.TextField(blank=True, null=True)
    precio_coto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_dia = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_jumbo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cafe'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PortfolioProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=100)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    link = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portfolio_project'"""
