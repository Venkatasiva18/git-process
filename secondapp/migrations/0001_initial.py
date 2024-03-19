# Generated by Django 5.0b1 on 2023-11-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('fee', models.FloatField()),
                ('addr', models.CharField(max_length=200)),
            ],
        ),
    ]