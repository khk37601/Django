from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import Serial_Premierleague, Serial_Detail_Premierleague
from .models import PremierLeague
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView,UpdateAPIView
from django.views.generic import View


#ListAPIView
class premier_league_list(viewsets.generics.ListCreateAPIView):
    queryset = PremierLeague.objects.all()
    serializer_class = Serial_Premierleague


class premier_league_detail_list(RetrieveAPIView):
    lookup_field = 'team_name'
    queryset = PremierLeague.objects.all()
    print(queryset)
    serializer_class = Serial_Detail_Premierleague


class PremierLeague_Delete(DestroyAPIView):

    queryset = PremierLeague.objects.all()
    serializer_class = Serial_Premierleague

    def get_object(self, pk):
        try:
            return PremierLeague.objects.get(team_name=pk)
        except:
            raise Http404

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object(kwargs['team_name'])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class PremierLeague_update(UpdateAPIView):

    queryset = PremierLeague.objects.all()
    serializer_class = Serial_Premierleague

    def get_object(self, pk):
        try:
            return PremierLeague.objects.get(team_name=pk)
        except:
            raise Http404

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)

        instance = self.get_object(kwargs['team_name'])
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
