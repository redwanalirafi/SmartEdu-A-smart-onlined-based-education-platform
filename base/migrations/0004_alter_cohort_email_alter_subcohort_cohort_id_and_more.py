# Generated by Django 4.1.3 on 2022-12-06 13:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_cohort_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cohort',
            name='email',
            field=models.ForeignKey(db_constraint=False, default='0', on_delete=django.db.models.deletion.CASCADE, to='base.userdata'),
        ),
        migrations.AlterField(
            model_name='subcohort',
            name='cohort_id',
            field=models.ForeignKey(db_constraint=False, default=0, on_delete=django.db.models.deletion.CASCADE, related_name='subcohortid', to='base.cohort'),
        ),
        migrations.AlterField(
            model_name='subcohort',
            name='parent_id',
            field=models.ForeignKey(db_constraint=False, default=0, on_delete=django.db.models.deletion.CASCADE, related_name='subparentid', to='base.cohort'),
        ),
        migrations.CreateModel(
            name='Cohortpdfs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, validators=[django.core.validators.MaxLengthValidator(100)])),
                ('content', models.FileField(upload_to='')),
                ('cohort_id', models.ForeignKey(db_constraint=False, default=0, on_delete=django.db.models.deletion.CASCADE, to='base.cohort')),
            ],
        ),
    ]
