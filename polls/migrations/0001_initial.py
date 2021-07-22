# Generated by Django 3.2.4 on 2021-07-22 14:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buffet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название курса')),
                ('mentor', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ментор')),
                ('assistant', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ассистент')),
                ('classroom', models.CharField(blank=True, max_length=255, null=True, verbose_name='Аудитория')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата начало курса')),
                ('end_date', models.DateTimeField(default=datetime.datetime(2999, 12, 31, 0, 0), verbose_name='Дата окончания курса')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('time', models.CharField(default='08:00', max_length=50, verbose_name='Время')),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('total_sum', models.FloatField()),
                ('debt_sum', models.FloatField()),
                ('status', models.IntegerField(choices=[(1, 'Оплачен'), (2, 'Не оплачен'), (3, 'Списан')])),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('pin', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('debt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('pin', models.CharField(max_length=6, verbose_name='Пин-код')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('pin', models.CharField(max_length=6, verbose_name='Пин-код')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.course')),
            ],
        ),
        migrations.CreateModel(
            name='OperationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=255)),
                ('buffet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.buffet')),
                ('operations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.operation')),
            ],
        ),
        migrations.AddField(
            model_name='operation',
            name='pin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.pin'),
        ),
    ]