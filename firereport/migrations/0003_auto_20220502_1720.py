
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firereport', '0002_auto_20220502_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firetequesthistory',
            name='firereport',
        ),
        migrations.DeleteModel(
            name='Firereport',
        ),
    ]