from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView
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
        team1 = GameTeam(context['object'].team1.team_posession, 
        context['object'].team1.team_hit,
         context['object'].team1.team_name)
        team2 = GameTeam(context['object'].team2.team_posession, 
        context['object'].team2.team_hit,
        context['object'].team2.team_name)        
        (result, mean, std) = simulate(nrOfRuns=context['object'].number_runs, team1=team1, team2=team2)
        # print(result[:,0])
        graph = get_plot(result[:,0],result[:,1])
        # print(result.shape[0])
        context['len'] = list(range(1,result.shape[0]+1))
        context['result1'] = result[:,0]
        context['result2'] = result[:,1]
        context['mean'] = mean
        context['std'] = std 
        context['graph']= graph
        context['win_loss'] = check_win_loss(result[:,0], result[:,1],context['object'].team1.team_name, context['object'].team2.team_name)
        obj = context['object']
        save_query(obj,mean,std)
        return context

def check_win_loss(x,y,n1="T1",n2="T2"):
    print(n1[0])
    n1 = n1[0]
    temp_n2 = n2[0]
    if(n1 == temp_n2):
        n2 = temp_n2 +str(1)
    else:
        n2 = temp_n2
    temp = []
    count = 0
    draw1 = 0
    for i in range(len(x)):
        if(x[i]>y[i]):
            count+=1
            win = (n1,"T1")
            temp.append(win)
        elif(x[i]<y[i]):
            loss = (n2,"T2")
            temp.append(loss)
        else:
            draw1+=1
            draw = ("Draw","Dr")
            temp.append(draw)
    # print(temp)
    return temp

def save_query(obj,mean,std):
    obj.avg_goal_1 = mean[0]
    obj.avg_goal_2 = mean[1]
    obj.std_goal_1 = std[0]
    obj.std_goal_2 = std[1]
    obj.save()


class TeamUpdate(UpdateView):
    model = Team
    success_url=reverse_lazy('sports_analytics:home')
    form_class = TeamForm
    template_name = "create_team.html"
