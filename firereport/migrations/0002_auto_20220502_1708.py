

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firereport', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firereport',
            old_name='Messgae',
            new_name='Message',
        ),
    ]
