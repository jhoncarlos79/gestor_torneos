# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Deportes(models.Model):
    id_deporte = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    num_jugadores = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'deportes'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

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


class Equipos(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_usuario = models.ForeignKey('UsersUser', models.DO_NOTHING, db_column='id_usuario')
    fecha = models.DateTimeField()
    id_deporte = models.ForeignKey(Deportes, models.DO_NOTHING, db_column='id_deporte')
    escudo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'equipos'


class Incripciones(models.Model):
    id_inscripciones = models.AutoField(primary_key=True)
    id_equipo = models.ForeignKey(Equipos, models.DO_NOTHING, db_column='id_equipo')
    id_torneo = models.ForeignKey('Torneos', models.DO_NOTHING, db_column='id_torneo')
    fecha_inscripcion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'incripciones'


class Jugadores(models.Model):
    id_jugador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    estatura = models.FloatField()
    peso = models.IntegerField()
    id_equipo = models.ForeignKey(Equipos, models.DO_NOTHING, db_column='id_equipo')
    fecha_vinculacion = models.DateTimeField()
    foto = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'jugadores'


class Partidos(models.Model):
    id_partido = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.DateTimeField()
    lugar = models.CharField(max_length=100)
    id_torneo = models.ForeignKey('Torneos', models.DO_NOTHING, db_column='id_torneo')
    id_equipo1 = models.ForeignKey(Equipos, models.DO_NOTHING, db_column='id_equipo1')
    id_equipo2 = models.ForeignKey(Equipos, models.DO_NOTHING, db_column='id_equipo2', related_name='partidos_id_equipo2_set')
    resultado_equipo1 = models.IntegerField()
    resultado_equipo2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'partidos'


class Torneos(models.Model):
    id_torneo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    id_deporte = models.ForeignKey(Deportes, models.DO_NOTHING, db_column='id_deporte')

    class Meta:
        managed = False
        db_table = 'torneos'


class UsersUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)
