# Generated by Django 4.1.6 on 2023-02-13 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_name', models.CharField(max_length=200)),
                ('house_number', models.IntegerField()),
                ('area', models.CharField(max_length=200)),
                ('flat_size', models.IntegerField()),
                ('flat_rent', models.IntegerField()),
                ('bad', models.IntegerField()),
                ('bath', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat_category', to='flat.category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
