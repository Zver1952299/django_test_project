# Generated by Django 5.1.1 on 2024-09-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('anons', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
