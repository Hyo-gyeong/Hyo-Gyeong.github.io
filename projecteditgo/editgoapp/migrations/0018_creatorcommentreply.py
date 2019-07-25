# Generated by Django 2.1.8 on 2019-07-20 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editgoapp', '0017_auto_20190720_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatorCommentReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccontents', models.CharField(max_length=500)),
                ('ccomment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creplys', to='editgoapp.Comment')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
