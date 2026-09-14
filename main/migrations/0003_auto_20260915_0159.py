from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_project_id'),
    ]

    operations = [
        migrations.RunSQL(
            "CREATE TABLE IF NOT EXISTS main_project (id SERIAL PRIMARY KEY, title VARCHAR(200) NOT NULL, role VARCHAR(200) NOT NULL, description TEXT NOT NULL, tech_stack VARCHAR(200) NOT NULL, image_url VARCHAR(200) NOT NULL);",
            "DROP TABLE IF EXISTS main_project;"
        ),
        migrations.RunSQL(
            "CREATE TABLE IF NOT EXISTS main_experience (id SERIAL PRIMARY KEY, role VARCHAR(200) NOT NULL, company VARCHAR(200) NOT NULL, duration VARCHAR(100) NOT NULL, description TEXT NOT NULL);",
            "DROP TABLE IF EXISTS main_experience;"
        ),
    ]