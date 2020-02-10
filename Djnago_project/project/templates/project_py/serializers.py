
from rest_framework import serializers
from  ...models import PremierLeague2


class Premierleague_2(serializers.ModelSerializer):
    class Meta:
        model = PremierLeague2
        fields =(

            'Rank',
            'Team',
            'winning',
        )