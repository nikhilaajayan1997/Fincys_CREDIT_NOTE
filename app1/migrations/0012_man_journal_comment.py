# Generated by Django 3.2.22 on 2023-10-11 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20231011_0428'),
    ]

    operations = [
        migrations.CreateModel(
            name='man_Journal_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('proj', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.mjournal')),
            ],
        ),
    ]
