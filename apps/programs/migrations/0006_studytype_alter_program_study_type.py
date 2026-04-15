from django.db import migrations, models
import django.db.models.deletion


def create_study_types_and_migrate(apps, schema_editor):
    StudyType = apps.get_model('programs', 'StudyType')
    Program = apps.get_model('programs', 'Program')

    # Create default study types
    ft, _ = StudyType.objects.get_or_create(
        slug='full-time',
        defaults={'name': 'Full-time', 'name_uz': 'Kunduzgi', 'name_ru': 'Очная'}
    )
    pt, _ = StudyType.objects.get_or_create(
        slug='part-time',
        defaults={'name': 'Part-time', 'name_uz': 'Sirtqi', 'name_ru': 'Заочная'}
    )
    ev, _ = StudyType.objects.get_or_create(
        slug='evening',
        defaults={'name': 'Evening', 'name_uz': 'Kechki', 'name_ru': 'Вечерняя'}
    )

    # Map old values to new FK
    mapping = {'full-time': ft.pk, 'part-time': pt.pk}
    for prog in Program.objects.all():
        old_val = prog.study_type_old
        if old_val in mapping:
            prog.study_type_new_id = mapping[old_val]
            prog.save(update_fields=['study_type_new_id'])


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0005_program_faculty_alter_program_department'),
    ]

    operations = [
        # Step 1: Create StudyType model
        migrations.CreateModel(
            name='StudyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_uz', models.CharField(blank=True, max_length=100)),
                ('name_ru', models.CharField(blank=True, max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Study Type',
                'verbose_name_plural': 'Study Types',
                'ordering': ['name'],
            },
        ),
        # Step 2: Rename old study_type to study_type_old
        migrations.RenameField(
            model_name='program',
            old_name='study_type',
            new_name='study_type_old',
        ),
        # Step 3: Add new FK field
        migrations.AddField(
            model_name='program',
            name='study_type_new',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='programs', to='programs.studytype'),
        ),
        # Step 4: Migrate data
        migrations.RunPython(create_study_types_and_migrate, migrations.RunPython.noop),
        # Step 5: Remove old field
        migrations.RemoveField(
            model_name='program',
            name='study_type_old',
        ),
        # Step 6: Rename new field
        migrations.RenameField(
            model_name='program',
            old_name='study_type_new',
            new_name='study_type',
        ),
    ]
