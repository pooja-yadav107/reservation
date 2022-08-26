# Generated by Django 4.0.6 on 2022-08-26 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buses', '0005_alter_seat_seat_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='seat_available',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='seat_booked_time',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='seta_book_by',
        ),
        migrations.AlterField(
            model_name='seat',
            name='seat_no',
            field=models.CharField(max_length=10),
        ),
        migrations.CreateModel(
            name='Seat_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_no', models.CharField(max_length=10)),
                ('seat_available', models.BooleanField(default=True)),
                ('seat_booked_time', models.DateTimeField(blank=True, null=True)),
                ('seta_book_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='bus',
            name='seat',
            field=models.ManyToManyField(to='buses.seat_details'),
        ),
    ]