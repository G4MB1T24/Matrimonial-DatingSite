# Generated by Django 4.0.4 on 2022-06-05 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_age_alter_profile_religion'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='usersocial',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='usersocial1',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='religion',
            field=models.CharField(blank=True, choices=[('Any', 'Any'), ('Jain', 'Jain'), ('Sikh', 'Sikh'), ('Buddhist', 'Buddhist'), ('Muslim', 'Muslim'), ('Hindu', 'Hindu'), ('Christian', 'Christian')], default=('Any', 'Any'), max_length=30, null=True),
        ),
    ]
