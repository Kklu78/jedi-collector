# Generated by Django 3.2.8 on 2021-10-22 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('F', 'Force'), ('L', 'Lightsaber'), ('M', 'Mind Tricks')], default='F', max_length=1)),
                ('jedi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.jedi')),
            ],
        ),
    ]
