# Generated by Django 3.1.4 on 2020-12-19 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_auto_20201219_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_data',
            name='student_id',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
