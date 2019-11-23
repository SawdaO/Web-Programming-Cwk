# Generated by Django 2.2.7 on 2019-11-21 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webay', '0004_auto_20191118_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webay.Item'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
