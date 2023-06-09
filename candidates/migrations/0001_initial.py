# Generated by Django 4.1.7 on 2023-03-10 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=30)),
                ('expected_salary', models.IntegerField()),
                ('will_relocate', models.BooleanField(default=False)),
            ],
        ),
    ]
