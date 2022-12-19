# Generated by Django 4.1.3 on 2022-12-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=1, max_digits=20)),
                ('image', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('lte_exists', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
    ]