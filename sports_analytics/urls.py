from django.urls import path, reverse_lazy
from .views import ResultCreate, TeamCreate, TeamView, home, ResultDetailView, TeamUpdate, ResultView, ResultDeleteView
app_name = "sports_analytics"

urlpatterns = [
    path('create-team/',TeamCreate.as_view(), name="createTeam"),
    path("home/",home ,name='home'),
    path("view-teams/",TeamView.as_view(), name='viewTeam'),
    path('select-team/',ResultCreate.as_view(),name='simulate'),
    # path('home/<int:pk>/', home_, name='test'),
    path('simulation-details/<int:pk>/',ResultDetailView.as_view(), name="result_detail"),
    path('update-team/<int:pk>/', TeamUpdate.as_view(), name="update_team"),
    path('results/', ResultView.as_view(), name="result"),
    path('delete-result/<int:pk>', ResultDeleteView.as_view(), name='delete-result'),
]