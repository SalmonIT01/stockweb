# Generated by Django 4.2.2 on 2023-11-13 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0004_rename_unit_id_details_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('m_id', models.AutoField(primary_key=True, serialize=False)),
                ('m_name', models.CharField(max_length=125, null=True)),
                ('m_phone', models.CharField(max_length=50, null=True)),
                ('products_set', models.ManyToManyField(to='app_home.details')),
            ],
        ),
    ]
