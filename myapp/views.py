from rest_framework import serializers
from .models import Player, Team
from rest_framework.response import Response
from rest_framework.decorators import api_view




class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


@api_view(['GET'])
def all_players(req):
    all_players = PlayerSerializer(Player.objects.all(), many=True).data
    return Response(all_players)