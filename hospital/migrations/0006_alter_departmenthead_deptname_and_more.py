# Generated by Django 4.2 on 2023-04-23 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_alter_departmenthead_deptname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmenthead',
            name='deptname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employees',
            name='deptname',
            field=models.CharField(max_length=200),
        ),
    ]
