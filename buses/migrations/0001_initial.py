# Generated by Django 4.0.6 on 2022-08-24 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(choices=[('Volvo', 'Volvo'), ('Kartar', 'Kartar'), ('Mercedez-benz', 'Mercedez-benz'), ('Roadways', 'Roadways')], default='test', max_length=60, null=True)),
                ('bus_type', models.CharField(choices=[('Regualar', 'Regualar'), ('AC', 'AC')], default='test', max_length=60, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('available_seats', models.IntegerField()),
                ('destination_from', models.CharField(max_length=50)),
                ('destination_to', models.CharField(max_length=50)),
            ],
        ),
    ]