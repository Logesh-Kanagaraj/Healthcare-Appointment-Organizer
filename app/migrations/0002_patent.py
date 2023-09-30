# Generated by Django 4.2.2 on 2023-06-19 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('mobno', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=20)),
                ('patdt', models.DateTimeField()),
                ('docname', models.CharField(max_length=20)),
                ('prpse', models.CharField(max_length=20)),
            ],
        ),
    ]