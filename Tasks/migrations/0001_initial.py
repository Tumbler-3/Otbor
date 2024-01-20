# Generated by Django 5.0 on 2024-01-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]