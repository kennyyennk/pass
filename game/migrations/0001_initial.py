# Generated by Django 3.2.8 on 2022-01-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=20, verbose_name='颜色名称')),
                ('color_times', models.IntegerField(verbose_name='使用次数')),
            ],
            options={
                'verbose_name': '颜色及使用次数',
                'verbose_name_plural': '颜色及使用次数',
                'db_table': 'colors_and_times',
            },
        ),
    ]