
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firereport', '0005_auto_20220503_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='firereport',
            name='AssignedTime',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
