# Generated by Django 3.1.6 on 2022-07-18 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('nickname', models.CharField(max_length=128)),
                ('position', models.CharField(max_length=128)),
                ('subjects', models.CharField(max_length=128)),
                ('image', models.ImageField(default='default.png', upload_to='profile/')),
            ],
        ),
    ]
