# Generated by Django 2.0 on 2018-01-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiuYan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
