# Generated by Django 3.1.7 on 2021-08-04 16:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_name', models.CharField(max_length=100)),
                ('scan_type', models.CharField(choices=[('Full Scan', 'Full Scan'), ('Subdomain', 'Subdomain'), ('Dirsearch', 'Dirsearch'), ('Wayback URL', 'Wayback URL'), ('JS File Discovery', 'JS File Discovery'), ('Secret/API key', 'Secret/API key'), ('Endpoint from JS', 'Endpoint from JS')], max_length=50)),
                ('domain_url', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Invalid format', regex='([a-z0-9]{2,}\\.)+[a-z0-9]{2,5}')])),
                ('is_bookmark', models.IntegerField(default=0)),
                ('scan_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResultFileName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('scan_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scanEngine.scan')),
            ],
        ),
    ]
