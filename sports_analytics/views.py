from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView
from .models import Result, Team
from .forms import ResultForm, TeamForm
from .simulate_games import simulate, GameTeam
from .utils import get_plot
# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello World</h1>")

class TeamCreate(CreateView):
    success_url=reverse_lazy('sports_analytics:home')
    model = Team
    template_name = "create_team.html"
    form_class = TeamForm

class TeamView(ListView):
    model = Team
    template_name = "sports_analytics/team_detail.html"

class ResultCreate(CreateView):
    model = Result
    template_name = "create_team.html"
    form_class = ResultForm

    def get_success_url(self):
        id = self.object.id
        return reverse_lazy('sports_analytics:result_detail', kwargs={'pk': id})


class ResultDetailView(DetailView):
    model = Result

    def get_context_data(self,*args,**kwargs):
        context =  super(ResultDetailView, self).get_context_data(*args,**kwargs)
        number_runs = context['object'].number_runs
        team1_name = context['object'].team1.team_name
        team2_name = context['object'].team2.team_name
        team1_p = context['object'].team1.team_posession
        team2_p = context['object'].team2.team_posession
        team1_h = context['object'].team1.team_hit
        team2_h = context['object'].team2.team_hit
        team1 = GameTeam(team1_p, team1_h, team1_name)
        team2 = GameTeam(team2_p, team2_h, team2_name)
        (result, mean, std) = simulate(nrOfRuns=number_runs, team1=team1, team2=team2)
        # print(result[:,0])
        graph = get_plot(result[:,0],result[:,1])
        context['result'] = result
        context['mean'] = mean
        context['std']= std
        context['graph']= graph
        return context
