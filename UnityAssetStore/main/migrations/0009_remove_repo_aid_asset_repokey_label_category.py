# Generated by Django 4.0.2 on 2022-02-16 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_description_asset_versionnum_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repo',
            name='AID',
        ),
        migrations.AddField(
            model_name='asset',
            name='RepoKey',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.repo'),
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LabelName', models.CharField(max_length=100)),
                ('AID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.asset')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=100)),
                ('AID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.asset')),
            ],
        ),
    ]