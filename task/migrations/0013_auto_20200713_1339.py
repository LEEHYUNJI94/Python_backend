# Generated by Django 3.0.6 on 2020-07-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0012_auto_20200713_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.SmallIntegerField(choices=[(1, 'high'), (2, 'middle'), (3, 'low')], default='middle'),
        ),
    ]
