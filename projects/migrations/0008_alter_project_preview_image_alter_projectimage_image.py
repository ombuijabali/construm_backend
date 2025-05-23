# Generated by Django 5.0.7 on 2024-09-12 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0007_alter_blog_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="preview_image",
            field=models.ImageField(upload_to="projects/"),
        ),
        migrations.AlterField(
            model_name="projectimage",
            name="image",
            field=models.ImageField(upload_to="project_images/"),
        ),
    ]
