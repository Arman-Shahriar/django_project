
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firereport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=250, null=True)),
                ('MobileNumber', models.CharField(max_length=12, null=True)),
                ('Location', models.CharField(max_length=200, null=True)),
                ('Messgae', models.CharField(max_length=200, null=True)),
                ('AssignTo', models.CharField(max_length=150, null=True)),
                ('Status', models.CharField(max_length=150, null=True)),
                ('Postingdate', models.DateField(null=True)),
                ('AssignTime', models.TimeField(null=True)),
                ('UpdationDate', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName', models.CharField(max_length=200, null=True)),
                ('teamLeaderName', models.CharField(max_length=250, null=True)),
                ('teamLeadMobno', models.CharField(max_length=15, null=True)),
                ('teamMembers', models.CharField(max_length=300, null=True)),
                ('postingDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Firetequesthistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200, null=True)),
                ('remark', models.CharField(max_length=250, null=True)),
                ('postingDate', models.DateTimeField(auto_now_add=True)),
                ('firereport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firereport.firereport')),
            ],
        ),
    ]
