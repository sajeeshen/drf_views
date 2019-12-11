# Generated by Django 3.0 on 2019-12-11 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(default=None, max_length=200, null=True)),
                ('author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_author', to='core.Author')),
            ],
        ),
    ]
