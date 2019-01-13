# Generated by Django 2.0.7 on 2018-10-10 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_load_target_table_and_columns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleanedfile',
            name='file',
            field=models.FileField(upload_to='cleaned-files'),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(upload_to='uploaded-files'),
        ),
    ]
