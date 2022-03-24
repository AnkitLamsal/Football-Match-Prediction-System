from django import forms
from .models import Team,Result

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name','team_hit','team_posession']


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['team1','team2','number_runs']
