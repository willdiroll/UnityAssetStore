# Generated by Django 4.0.1 on 2022-02-13 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_delete_class_asset_delete_class_info_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AID', models.IntegerField()),
                ('AssetName', models.CharField(max_length=100)),
                ('AssetLink', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
                ('Version', models.CharField(max_length=100)),
                ('ImgLink', models.CharField(max_length=100)),
                ('Keywords', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='repo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RepoKey', models.IntegerField()),
                ('Name', models.CharField(max_length=100)),
                ('Identifier', models.CharField(max_length=100)),
                ('AID', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='asset_info',
        ),
    ]