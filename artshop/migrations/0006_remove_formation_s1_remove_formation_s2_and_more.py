# Generated by Django 4.2.3 on 2023-08-29 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artshop', '0005_formation_delete_formnew'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formation',
            name='s1',
        ),
        migrations.RemoveField(
            model_name='formation',
            name='s2',
        ),
        migrations.AddField(
            model_name='formation',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='formation',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
