# Generated by Django 2.1.8 on 2019-07-12 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editgoapp', '0010_auto_20190713_0341'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatorComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField()),
                ('cblog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='editgoapp.Creator')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
