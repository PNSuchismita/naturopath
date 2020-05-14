# Generated by Django 2.2.7 on 2019-12-20 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_auto_20191217_0712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='date',
        ),
        migrations.AddField(
            model_name='appointment',
            name='fees',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='txnid',
            field=models.CharField(max_length=40, null=True),
        ),
    ]