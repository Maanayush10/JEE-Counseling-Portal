# Generated by Django 4.2 on 2023-04-24 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rankerApp", "0002_alter_signup_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signup", name="email", field=models.EmailField(max_length=100),
        ),
    ]