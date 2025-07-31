from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from .models import Greeting
import requests
import os
import json
# Create your views here.


def index(request):
    print(request)
    #files = os.listdir(r"\\prod.factset.com\dfs\CCS-Application\holdings\CCAutomation")
    files_json = json.dumps([os.getenv("AWS_ACCESS_KEY_ID")])
    return HttpResponse('<pre>' + files_json+ '</pre>')

@api_view(['POST'])
def conv(request):
    print(request)
    #files = os.listdir(r"\\prod.factset.com\dfs\CCS-Application\holdings\CCAutomation")
    #files_json = json.dumps([os.getenv("AWS_ACCESS_KEY_ID")])
    #return HttpResponse('<pre>' + files_json+ '</pre>')
    return HttpResponse(request.FILES["file"], content_type="application/pdf")

def db(request):
    # If you encounter errors visiting the `/db/` page on the example app, check that:
    #
    # When running the app on Heroku:
    #   1. You have added the Postgres database to your app.
    #   2. You have uncommented the `psycopg` dependency in `requirements.txt`, and the `release`
    #      process entry in `Procfile`, git committed your changes and re-deployed the app.
    #
    # When running the app locally:
    #   1. You have run `./manage.py migrate` to create the `hello_greeting` database table.

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
