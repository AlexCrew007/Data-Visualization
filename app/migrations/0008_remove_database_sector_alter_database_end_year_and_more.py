# Generated by Django 4.2.1 on 2023-05-05 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_database_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='database',
            name='sector',
        ),
        migrations.AlterField(
            model_name='database',
            name='end_year',
            field=models.IntegerField(default=2023, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='intensity',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='likelihood',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='relevance',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='start_year',
            field=models.IntegerField(default=2023, null=True),
        ),
    ]
