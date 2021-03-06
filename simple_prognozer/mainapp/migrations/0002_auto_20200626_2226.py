# Generated by Django 3.0.1 on 2020-06-26 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintable',
            name='combined_key',
            field=models.CharField(default='us', max_length=128, unique=True, verbose_name='Combined_key'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='maintable',
            name='last_update',
            field=models.CharField(max_length=128, verbose_name='Last_update'),
        ),
        migrations.CreateModel(
            name='TimeSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField()),
                ('confirmed', models.PositiveIntegerField(default=0, verbose_name='Confirmed')),
                ('deaths', models.PositiveIntegerField(default=0, verbose_name='Deaths')),
                ('recovered', models.PositiveIntegerField(default=0, verbose_name='Recovered')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.MainTable')),
            ],
        ),
    ]
