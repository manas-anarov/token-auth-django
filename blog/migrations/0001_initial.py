# Generated by Django 2.2.9 on 2019-12-30 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=0, max_length=400)),
                ('text', models.CharField(default=0, max_length=400)),
            ],
        ),
    ]
