# Generated by Django 4.2.7 on 2025-04-06 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=400)),
                ('completed', models.BooleanField(default=False)),
                ('cretaedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
