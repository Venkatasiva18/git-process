# Generated by Django 5.0b1 on 2023-12-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('taste', models.CharField(max_length=120)),
                ('color', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
