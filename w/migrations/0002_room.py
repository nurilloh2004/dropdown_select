# Generated by Django 4.1 on 2022-09-18 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('w', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='w.module')),
            ],
        ),
    ]
