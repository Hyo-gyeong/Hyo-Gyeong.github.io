# Generated by Django 2.1.8 on 2019-07-19 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editgoapp', '0013_auto_20190714_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creatorcomment',
            old_name='contents',
            new_name='ccontents',
        ),
    ]
