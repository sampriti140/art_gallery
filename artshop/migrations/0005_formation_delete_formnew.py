# Generated by Django 4.2.3 on 2023-08-29 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artshop', '0004_formnew_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s1', models.CharField(default='', max_length=50)),
                ('s2', models.CharField(default='', max_length=200)),
            ],
            options={
                'db_table': 'formation',
            },
        ),
        migrations.DeleteModel(
            name='formnew',
        ),
    ]