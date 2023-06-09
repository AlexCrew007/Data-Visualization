# Generated by Django 4.2.1 on 2023-05-04 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.CharField(max_length=255)),
                ('intensity', models.IntegerField()),
                ('sector', models.CharField(max_length=255)),
                ('topic', models.CharField(max_length=255)),
                ('insight', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('region', models.CharField(max_length=255)),
                ('start_year', models.CharField(max_length=255)),
                ('impact', models.CharField(max_length=255)),
                ('added', models.DateTimeField()),
                ('published', models.DateTimeField()),
                ('country', models.CharField(max_length=255)),
                ('relevance', models.IntegerField()),
                ('pestle', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('likelihood', models.IntegerField()),
            ],
        ),
    ]
