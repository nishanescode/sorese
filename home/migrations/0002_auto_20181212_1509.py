# Generated by Django 2.1.4 on 2018-12-12 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='description',
            name='descrption_title',
            field=models.CharField(max_length=180),
        ),
    ]
