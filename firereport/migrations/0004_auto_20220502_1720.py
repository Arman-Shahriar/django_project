
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firereport', '0003_auto_20220502_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firereport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=250, null=True)),
                ('MobileNumber', models.CharField(max_length=12, null=True)),
                ('Location', models.CharField(max_length=200, null=True)),
                ('Message', models.CharField(max_length=200, null=True)),
                ('AssignTo', models.CharField(max_length=150, null=True)),
                ('Status', models.CharField(max_length=150, null=True)),
                ('Postingdate', models.DateTimeField(auto_now_add=True)),
                ('UpdationDate', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='firetequesthistory',
            name='firereport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firereport.firereport'),
        ),
    ]
