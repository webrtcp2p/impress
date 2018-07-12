from django.shortcuts import render
from django.http import HttpResponse
from .resources import PersonResource
from .models import *

def impress(request):


	ob = Impress(
					candidateNumber = request.POST['q51_candidateNumber'],
					Department = request.POST['q53_department'],
					registerNumber = request.POST['q52_registerNumber'],

					Greet = request.POST['q60_input60[0]'],
					Attitude = request.POST['q60_input60[1]'],
					Dressed = request.POST['q60_input60[2]'],
					Enthusiasm  = request.POST['q60_input60[3]'],
					Confidence = request.POST['q60_input60[4]'],
					KnowledgeofJobRoles = request.POST['q60_input60[5]'],
					Education = request.POST['q60_input60[6]'],
					RelatedExperience = request.POST['q60_input60[7]'],
					AnsweredQuestionsWell = request.POST['q60_input60[8]'],
					Answersfocusedonstrengths = request.POST['q60_input60[9]'],
					TeamSkills = request.POST['q60_input60[10]'],
					CommunicationSkills = request.POST['q60_input60[11]'],
					NonVerbal = request.POST['q60_input60[12]'],
					ListeningSkills = request.POST['q60_input60[13]'],
					ResumeConstruction = request.POST['q60_input60[14]'],
					ChoiceofAreaofInterest = request.POST['q60_input60[15]'],
					TechnicalCompetency = request.POST['q60_input60[16]'],
					AskedGoodQuestions = request.POST['q60_input60[18]'],
					ThankedInterviewer = request.POST['q60_input60[19]'],
					comments = request.POST['q37_comments'],
					selected = request.POST['q54_selected'],
					hrName = request.POST['q55_techHr55'])

	ob.save()





	return render(request,"impress.html",{})
	
def download(request): 
	person_resource = PersonResource()
	dataset = person_resource.export()
	response = HttpResponse(dataset.csv, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="Reports.csv"'
	return response

	


