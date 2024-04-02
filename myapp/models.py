from django.db import models

# models.py
from django.db import models

class Team(models.Model):
    team_id = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=3)

    def __str__(self):
        return self.full_name

class Player(models.Model):
    player_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

