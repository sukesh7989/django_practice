# Generated by Django 5.0.10 on 2024-12-20 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vedaitapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='fees',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='admission',
            name='joindate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='admission',
            name='stu_class',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
