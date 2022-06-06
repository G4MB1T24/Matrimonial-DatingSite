# Generated by Django 4.0.4 on 2022-06-06 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_profile_religion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='religion',
            field=models.CharField(blank=True, choices=[('Sikh', 'Sikh'), ('Jain', 'Jain'), ('Any', 'Any'), ('Muslim', 'Muslim'), ('Hindu', 'Hindu'), ('Christian', 'Christian'), ('Buddhist', 'Buddhist')], default=('Any', 'Any'), max_length=30, null=True),
        ),
    ]