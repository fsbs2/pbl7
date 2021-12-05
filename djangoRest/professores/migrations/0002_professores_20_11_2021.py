# Generated by Django 3.2.7 on 2021-11-20 20:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('cod_curso', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplinas',
            fields=[
                ('cod_disciplina', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Professores',
            fields=[
                ('cod_professor', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome_professor', models.CharField(max_length=320)),
                ('ru', models.CharField(max_length=16)),
                ('matricula', models.IntegerField()),
                ('formacao', models.CharField(max_length=1024)),
                ('titulacao', models.CharField(max_length=1024)),
                ('area_titulacao', models.CharField(max_length=1024)),
                ('endereco_completo', models.CharField(max_length=512)),
                ('telefone_fixo', models.CharField(max_length=16)),
                ('whatsapp', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=64)),
                ('data_ingresso_instituicao', models.DateField(auto_now_add=True)),
                ('data_docencia', models.DateField(blank=True, null=True)),
                ('data_docencia_instituicao', models.DateField(blank=True, null=True)),
                ('funcao', models.CharField(max_length=128)),
                ('regime_trabalho', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina_Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professores.disciplinas')),
                ('cod_professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professores.professores')),
            ],
        ),
        migrations.CreateModel(
            name='Curso_Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professores.cursos')),
                ('cod_professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professores.professores')),
            ],
        ),
    ]