from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Serial_Premierleague, Serial_Detail_Premierleague
from .models import PremierLeague
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView,UpdateAPIView


#
class premier_league_list(ListAPIView):
    queryset = PremierLeague.objects.all()
    serializer_class = Serial_Premierleague


class premier_league_detail_list(RetrieveAPIView):
    lookup_field = 'team_name'
    queryset = PremierLeague.objects.all()
    serializer_class = Serial_Detail_Premierleague


class PremierLeague_Delete(DestroyAPIView):
    queryset = PremierLeague.objects.all()
    serializer_class = Serial_Premierleague

class PremierLeague_update(UpdateAPIView):
    queryset = PremierLeague.objects.all()
    serializer_class = Serial_Premierleague
