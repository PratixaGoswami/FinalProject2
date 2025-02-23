# Generated by Django 4.2 on 2024-12-22 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_add_worker_delete_hiree'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('skills', models.TextField()),
                ('exp', models.TextField()),
                ('location', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='add_worker',
        ),
    ]
