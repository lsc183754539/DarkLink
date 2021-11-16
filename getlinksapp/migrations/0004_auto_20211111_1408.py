# Generated by Django 3.2.8 on 2021-11-11 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getlinksapp', '0003_linksdata_find_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linksdata',
            name='abnormal',
            field=models.BooleanField(blank=True, null=True, verbose_name='是否异常'),
        ),
        migrations.AlterField(
            model_name='linksdata',
            name='abnormal_point',
            field=models.BooleanField(blank=True, null=True, verbose_name='异常点'),
        ),
        migrations.AlterField(
            model_name='linksdata',
            name='find_time',
            field=models.TimeField(blank=True, null=True, verbose_name='发现时间'),
        ),
        migrations.AlterField(
            model_name='linksdata',
            name='link',
            field=models.TextField(blank=True, null=True, verbose_name='链接'),
        ),
        migrations.AlterField(
            model_name='linksdata',
            name='response_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='响应状态码'),
        ),
        migrations.AlterField(
            model_name='mission',
            name='domain',
            field=models.TextField(blank=True, null=True, verbose_name='域'),
        ),
        migrations.AlterField(
            model_name='mission',
            name='url',
            field=models.TextField(blank=True, null=True, verbose_name='入口链接'),
        ),
    ]