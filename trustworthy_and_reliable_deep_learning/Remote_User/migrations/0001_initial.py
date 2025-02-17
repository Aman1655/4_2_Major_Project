# Generated by Django 5.1.5 on 2025-01-18 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientRegister_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=10)),
                ('phoneno', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='cyberattack_detection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fid', models.CharField(max_length=300)),
                ('Protocol', models.CharField(max_length=300)),
                ('Flag', models.CharField(max_length=300)),
                ('Packet', models.CharField(max_length=300)),
                ('Sender_ID', models.CharField(max_length=300)),
                ('Receiver_ID', models.CharField(max_length=300)),
                ('Source_IP_Address', models.CharField(max_length=300)),
                ('Destination_IP_Address', models.CharField(max_length=300)),
                ('Source_Port', models.CharField(max_length=300)),
                ('Destination_Port', models.CharField(max_length=300)),
                ('Packet_Size', models.CharField(max_length=300)),
                ('Prediction', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='detection_accuracy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=300)),
                ('ratio', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='detection_ratio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=300)),
                ('ratio', models.CharField(max_length=300)),
            ],
        ),
    ]
