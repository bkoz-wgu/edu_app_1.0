# Generated by Django 3.1.4 on 2020-12-22 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0014_auto_20201222_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_data',
            name='goal_score',
            field=models.CharField(default='n/a', max_length=3),
        ),
    ]
