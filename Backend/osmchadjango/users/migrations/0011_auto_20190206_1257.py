# Generated by Django 2.0.10 on 2019-02-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20190123_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappingteam',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='mappingteam',
            unique_together=set(),
        ),
    ]