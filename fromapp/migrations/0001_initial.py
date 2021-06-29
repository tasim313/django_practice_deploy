# Generated by Django 2.2.5 on 2021-06-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('ipaddress', models.GenericIPAddressField()),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
    ]