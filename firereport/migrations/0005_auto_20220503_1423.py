
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firereport', '0004_auto_20220502_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firereport',
            name='AssignTo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firereport.teams'),
        ),
    ]
