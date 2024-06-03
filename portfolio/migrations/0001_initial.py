# Generated by Django 4.2.7 on 2024-06-03 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homeslider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text1', models.CharField(blank=True, help_text='maximum of 40 charaters permitted', max_length=40, null=True)),
                ('text2', models.CharField(blank=True, help_text='maximum of 30 charaters permitted', max_length=30, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]