# Generated by Django 4.2.3 on 2023-08-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artshop', '0003_remove_user_artworks_remove_user_phoneno_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='formnew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s1', models.CharField(default='', max_length=50)),
                ('s2', models.CharField(default='', max_length=200)),
            ],
            options={
                'db_table': 'formnew',
            },
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
