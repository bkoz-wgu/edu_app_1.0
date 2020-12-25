# Generated by Django 3.1.4 on 2020-12-19 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_auto_20201219_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=60)),
                ('category_description', models.CharField(max_length=400)),
            ],
        ),
        migrations.RemoveField(
            model_name='question_data',
            name='question_category',
        ),
        migrations.CreateModel(
            name='Cat_Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.category')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.question_data')),
            ],
        ),
        migrations.AddField(
            model_name='question_data',
            name='categories',
            field=models.ManyToManyField(through='tests.Cat_Assignment', to='tests.Category'),
        ),
    ]