# Generated by Django 3.1.4 on 2020-12-20 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_auto_20201220_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_data',
            name='average_t4',
            field=models.CharField(default=50, max_length=3),
            preserve_default=False,
        ),
    ]
