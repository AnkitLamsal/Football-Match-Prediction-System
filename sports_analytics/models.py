from email.policy import default
from django.db import models


from django.core.validators import MaxValueValidator, MinValueValidator

min = 0.0
max = 1.0

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=50, unique=True)
    team_posession =  models.FloatField(validators=[MinValueValidator(min), MaxValueValidator(max)],)
    team_hit = models.FloatField(validators=[MinValueValidator(min), MaxValueValidator(max)],)

    def __str__(self):
        return f'{self.team_name}'


class Result(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.PROTECT)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.PROTECT)
    avg_goal_1 = models.IntegerField(default=0)
    avg_goal_2 = models.IntegerField(default=0)
    std_goal_1 = models.FloatField(default=0.0)
    std_goal_2 = models.FloatField(default=0.0)
    number_runs = models.PositiveIntegerField(default=0)
