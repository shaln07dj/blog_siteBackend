# Generated by Django 3.2.8 on 2022-03-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='bio',
            field=models.TextField(),
        ),
    ]