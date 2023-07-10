# Generated by Django 4.2.1 on 2023-07-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200, verbose_name='نام')),
                ('lastName', models.CharField(max_length=200, verbose_name='نام خانوادگی')),
                ('grade', models.CharField(max_length=200, verbose_name='پایه تحصیلی')),
                ('rank', models.CharField(max_length=200, verbose_name='رتبه')),
            ],
        ),
    ]