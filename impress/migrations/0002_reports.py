# Generated by Django 2.0.7 on 2018-07-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impress', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CandidateName', models.CharField(max_length=60)),
                ('Department', models.CharField(max_length=60)),
                ('RegisterNumber', models.CharField(max_length=60)),
                ('Attitude', models.CharField(max_length=60)),
                ('Enthusiasm', models.CharField(max_length=60)),
                ('Confidence', models.CharField(max_length=60)),
                ('Total1', models.CharField(max_length=60)),
                ('KnowledgeofJobRoles', models.CharField(max_length=60)),
                ('Education', models.CharField(max_length=60)),
                ('RelatedExperience', models.CharField(max_length=60)),
                ('AnsweredQuestionsWell', models.CharField(max_length=60)),
                ('Total2', models.CharField(max_length=60)),
                ('TeamSkills', models.CharField(max_length=60)),
                ('CommunicationSkills', models.CharField(max_length=60)),
                ('NonVerbal', models.CharField(max_length=60)),
                ('ListeningSkills', models.CharField(max_length=60)),
                ('Total3', models.CharField(max_length=60)),
                ('ResumeConstruction', models.CharField(max_length=60)),
                ('ChoiceofAreaofInterest', models.CharField(max_length=60)),
                ('Answersfocusedonstrengths', models.CharField(max_length=60)),
                ('Total4', models.CharField(max_length=60)),
                ('TechnicalCompetency', models.CharField(max_length=60)),
                ('Greet', models.CharField(max_length=60)),
                ('Dressed', models.CharField(max_length=60)),
                ('AskedGoodQuestions', models.CharField(max_length=60)),
                ('ThankedInterviewer', models.CharField(max_length=60)),
                ('Total5', models.CharField(max_length=60)),
                ('selected', models.CharField(max_length=60)),
                ('TotalScore', models.CharField(max_length=60)),
                ('comments', models.CharField(max_length=60)),
                ('selectedchar', models.CharField(max_length=60)),
                ('hrName', models.CharField(max_length=60)),
            ],
        ),
    ]
