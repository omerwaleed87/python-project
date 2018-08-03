# Generated by Django 2.0.7 on 2018-08-03 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationDivision',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('parent', models.IntegerField(default=0)),
                ('location_key', models.CharField(max_length=500)),
                ('level', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyTypes',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('parentId', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
