# Generated by Django 3.0 on 2019-12-30 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='Roles',
            field=models.CharField(choices=[('Scan', 'Freshman'), ('Phase 1', 'Sophomore'), ('Phase 2', 'Junior'), ('Phase 3', 'Senior'), ('Final', 'Graduate')], default='Scan', max_length=10),
        ),
    ]