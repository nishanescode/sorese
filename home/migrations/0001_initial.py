# Generated by Django 2.1.4 on 2018-12-12 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrption_title', models.CharField(max_length=200)),
                ('descrption_text', models.TextField()),
            ],
        ),
    ]
