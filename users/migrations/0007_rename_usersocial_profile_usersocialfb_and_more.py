# Generated by Django 4.0.4 on 2022-06-05 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_usersocial_profile_usersocial1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='usersocial',
            new_name='usersocialFB',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='usersocial1',
            new_name='usersocialINSTA',
        ),
        migrations.AddField(
            model_name='profile',
            name='usersocialTWT',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='religion',
            field=models.CharField(blank=True, choices=[('Hindu', 'Hindu'), ('Jain', 'Jain'), ('Any', 'Any'), ('Sikh', 'Sikh'), ('Christian', 'Christian'), ('Buddhist', 'Buddhist'), ('Muslim', 'Muslim')], default=('Any', 'Any'), max_length=30, null=True),
        ),
    ]