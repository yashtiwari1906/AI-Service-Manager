from django.shortcuts import render
from django.http import JsonResponse

from ai_service_manager.tasks import send_feedback_email_task
# Create your views here.

def home(request):
    send_feedback_email_task.delay("it's working!")
    return JsonResponse({"info": 'Django backend'})