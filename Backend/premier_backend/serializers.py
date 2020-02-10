from rest_framework import serializers
from .models import PremierLeague


class Serial_Premierleague(serializers.ModelSerializer):
    class Meta:
        model = PremierLeague
        fields = ('rank', 'team_name', 'winning',)

class Serial_Detail_Premierleague(serializers.ModelSerializer):
    class Meta:
        model = PremierLeague
        fields = ('rank', 'team_name', 'winning',)