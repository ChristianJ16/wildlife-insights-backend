# Generated by Django 4.2.13 on 2024-06-27 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlife', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('scientific_name', models.CharField(blank=True, max_length=255, null=True)),
                ('habitat', models.CharField(blank=True, max_length=255, null=True)),
                ('diet', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='favoritelist',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='favoritelist',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='favoritelist',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='favoritelist',
            name='animals',
            field=models.ManyToManyField(related_name='favorite_lists', to='wildlife.animal'),
        ),
    ]