# Generated by Django 2.1.8 on 2019-07-14 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editgoapp', '0012_auto_20190714_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creatorcomment',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ccomments', to='editgoapp.Creator'),
        ),
    ]
