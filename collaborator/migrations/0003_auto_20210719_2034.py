# Generated by Django 3.1 on 2021-07-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaborator', '0002_auto_20210719_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborator',
            name='position',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Project Admin'), (2, 'Project Manager'), (3, 'Project Leader'), (4, 'Member'), (5, 'Spectator')], default=4),
        ),
        migrations.AlterField(
            model_name='collaborator',
            name='status',
            field=models.CharField(choices=[('Invited', 'Onhold'), ('Joined', 'Joined'), ('Leaved', 'Leaved'), ('Removed', 'Removed'), ('Declined', 'Declined')], default='Invited', max_length=120, verbose_name='invite status'),
        ),
    ]
