from django.shortcuts import render, Http404
from django.views.generic import View
import json
import requests


# Create your views here.
def index(request):
   return render(request, 'front_html/premier_index.html')


class Search(View):

    def Post(self, request):
        pass

    def get(self, request):
        __url = 'http://127.0.0.1:8000/premier_league_list/{}/'.format(request.GET.get('user_date'))
        data = (requests.get(__url)).json()


        return render(request, 'front_html/premier_index.html',{'detail_team': data})



