# Generated by Django 2.2.7 on 2019-12-15 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_doctor_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultDetails',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='doctor.Doctor')),
                ('fees', models.IntegerField(null=True)),
                ('time', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
