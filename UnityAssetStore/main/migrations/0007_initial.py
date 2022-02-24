# Generated by Django 4.0.1 on 2022-02-15 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0006_remove_repo_aid_delete_asset_delete_repo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('AID', models.IntegerField(primary_key=True, serialize=False)),
                ('AssetName', models.CharField(max_length=100)),
                ('AssetLink', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
                ('Version', models.CharField(max_length=100)),
                ('ImgLink', models.CharField(max_length=100)),
                ('Keywords', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('RepoKey', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Identifier', models.CharField(max_length=100)),
                ('AID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.asset')),
            ],
        ),
    ]
