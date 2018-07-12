from django.db import models

class Impress(models.Model):
	candidateNumber = models.CharField((u'Candidate Name'),max_length=60)
	registerNumber = models.CharField((u'Register Number'),max_length=60)
	Department = models.CharField((u'Department'),max_length=5)

	Greet = models.CharField((u'Greeted Interviewer/Stated Name/Handshake/Good 1st Impression'),max_length=15)
	Attitude = models.CharField((u'Attitude'),max_length=15)
	Dressed = models.CharField((u'Dressed Well'),max_length=15)
	Enthusiasm = models.CharField((u'Enthusiasm'),max_length=15)
	Confidence = models.CharField((u'Confidence'),max_length=15)
	KnowledgeofJobRoles = models.CharField((u'Knowledge of Job Roles'),max_length=15)
	Education = models.CharField((u'Education'),max_length=15)
	RelatedExperience = models.CharField((u'Related Experience'),max_length=15)
	AnsweredQuestionsWell = models.CharField((u'Answered Questions Well'),max_length=15)
	Answersfocusedonstrengths = models.CharField((u'Answers focused on strengths'),max_length=15)
	TeamSkills = models.CharField((u'TeamSkills'),max_length=15)
	CommunicationSkills = models.CharField((u'Communication Skills'),max_length=15)
	NonVerbal = models.CharField((u'NonVerbal'),max_length=15)
	ListeningSkills = models.CharField((u'Listening Skills'),max_length=15)
	ResumeConstruction = models.CharField((u'Resume Construction'),max_length=15)
	ChoiceofAreaofInterest = models.CharField((u'Choice of Area of Interest'),max_length=15)
	TechnicalCompetency = models.CharField((u'Technical Competency'),max_length=15)
	AskedGoodQuestions = models.CharField((u'Asked Good Questions'),max_length=15)
	ThankedInterviewer = models.CharField((u'Thanked Interviewer'),max_length=15)

	comments = models.CharField((u'Comments'),max_length=200)
	selected = models.CharField((u'Selected'),max_length=3)
	hrName = models.CharField((u'HR Name'),max_length=35)
	date = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.candidateNumber

	class Meta:
		verbose_name_plural = "Impress"
