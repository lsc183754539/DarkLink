# Generated by Django 3.2.8 on 2021-11-11 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('getlinksapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linksdata',
            name='mission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mission', to='getlinksapp.mission', verbose_name='任务信息'),
        ),
    ]
