# Generated by Django 2.0.7 on 2018-07-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Impress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidateNumber', models.CharField(max_length=60, verbose_name='Candidate Name')),
                ('registerNumber', models.CharField(max_length=60, verbose_name='Register Number')),
                ('Department', models.CharField(max_length=5, verbose_name='Department')),
                ('Greet', models.CharField(max_length=15, verbose_name='Greeted Interviewer/Stated Name/Handshake/Good 1st Impression')),
                ('Attitude', models.CharField(max_length=15, verbose_name='Attitude')),
                ('Dressed', models.CharField(max_length=15, verbose_name='Dressed Well')),
                ('Enthusiasm', models.CharField(max_length=15, verbose_name='Enthusiasm')),
                ('Confidence', models.CharField(max_length=15, verbose_name='Confidence')),
                ('KnowledgeofJobRoles', models.CharField(max_length=15, verbose_name='Knowledge of Job Roles')),
                ('Education', models.CharField(max_length=15, verbose_name='Education')),
                ('RelatedExperience', models.CharField(max_length=15, verbose_name='Related Experience')),
                ('AnsweredQuestionsWell', models.CharField(max_length=15, verbose_name='Answered Questions Well')),
                ('Answersfocusedonstrengths', models.CharField(max_length=15, verbose_name='Answers focused on strengths')),
                ('TeamSkills', models.CharField(max_length=15, verbose_name='TeamSkills')),
                ('CommunicationSkills', models.CharField(max_length=15, verbose_name='Communication Skills')),
                ('NonVerbal', models.CharField(max_length=15, verbose_name='NonVerbal')),
                ('ListeningSkills', models.CharField(max_length=15, verbose_name='Listening Skills')),
                ('ResumeConstruction', models.CharField(max_length=15, verbose_name='Resume Construction')),
                ('ChoiceofAreaofInterest', models.CharField(max_length=15, verbose_name='Choice of Area of Interest')),
                ('TechnicalCompetency', models.CharField(max_length=15, verbose_name='Technical Competency')),
                ('AskedGoodQuestions', models.CharField(max_length=15, verbose_name='Asked Good Questions')),
                ('ThankedInterviewer', models.CharField(max_length=15, verbose_name='Thanked Interviewer')),
                ('comments', models.CharField(max_length=200, verbose_name='Comments')),
                ('selected', models.CharField(max_length=3, verbose_name='Selected')),
                ('hrName', models.CharField(max_length=35, verbose_name='HR Name')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Impress',
            },
        ),
    ]