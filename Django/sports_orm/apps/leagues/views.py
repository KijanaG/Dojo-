from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"ASC": League.objects.get(name="Atlantic Soccer Conference").teams.all(),
		"BPP": Team.objects.get(team_name="Penguins").curr_players.all(),
		"ICBCP": Team.objects.filter(league_id=2).all(),
		"ACAF": Team.objects.filter(league_id=7).all(),
		"Football": League.objects.filter(sport="Football").all(),
		"Flores": Player.objects.filter(last_name="Flores"),
		"Rough":Team.objects.get(team_name="Roughriders").id
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")