# Generated by Django 3.1.5 on 2023-04-02 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0007_question2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer1', models.CharField(choices=[('Assertive', 'Assertive'), ('Passive', 'Passive'), ('Agressive', 'Agressive'), ('Collaborative', 'Assertive'), ('Other', 'Other')], max_length=264, null=True)),
                ('answer2', models.CharField(choices=[('Avoidance', 'Avoidance'), ('Confrontation', 'Confrontation'), ('Compromise', 'Compromise'), ('Collaboration', 'Collaboration'), ('Other', 'Other')], max_length=264, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
