from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from .models import Greeting
import requests
import os
import json
from tabula.io import read_pdf
import pandas as pd

# Create your views here.


@api_view(['POST'])
def tabula(request):
    columns = json.loads(request.POST['columns'])

    dfs = read_pdf(
        request.FILES['file'],
        stream=True,
        pages='all',
        area=[0, 0, 100, 100],
        relative_area= True,
        columns=columns,
        relative_columns= True,
        multiple_tables= True,
        pandas_options= {"header": None}
    )

    # concatenate the dataframes to each other resulting to one dataframe
    df_out = pd.concat(dfs)

    # convert to excel without the headers and indices
    json_data = df_out.to_dict(orient="records")

    return JsonResponse(json_data, safe=False)


@api_view(['POST'])
def return_file(request):
    return HttpResponse(request.FILES["file"], content_type="application/pdf")
