# Generated by Django 3.1.3 on 2021-03-26 18:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_accountdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountdetail',
            name='ifsc',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]