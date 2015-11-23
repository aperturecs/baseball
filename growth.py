#coding:utf-8
from hitterProfile import HitterProfile
from hitterGame import HitterGame

def find(year, month):
    temps = []
    for game in games:
        if game.year == year and game.month:
            temps.append(game)
    return temps

Games = []

for year in range(2010,2015):
    for month in range(3,10):
        tempGame = {"year":year,"month":month,"OPS":0.0,"H":0,"BB":0,"HBP":0,"AB":0,"HBP":0,"TB":0}
        tempGames = find(year, month)
        for game in tempGames:
            tempGame["H"] += game.H
            tempGame["BB"]+= game.BB
            tempGame["HBP"]+= game.HBP
            tempGame["AB"]+=game.AB
            tempGame["TB"]+= game.H + game.2B*2 + game.3B*3 + game.HR*4
        Games.append(tempGame) # [{"year":year,"month":month,"OPS":0.0,"H":0,"BB":0,"HBP":0,"AB":0,"HBP":0,"TB":0}]

OPS_A = [] #매월 경기 OPS

for year in range(2010, 2015):
    for month in range(3, 10):
        for i in Games:
            if Games[i].get("year")==year and Games[i].get("month")==month:
                OBP = (Games[i].get("H") + Games[i].get("BB") + Games[i].get("HBP"))/(Games[i].get("AB") + Games[i].get("BB") + Games[i].get("HBP"))
                SLG = Games[i].get("TB")/Games[i].get("AB")
                OPS = OBP + SLG
                OPS_A.append({"year":year, "month":month, "ops":OPS}) #계산한 OPS 매월별 집어넣기

OPS_y =[] #OPS 성장률 y값
OPS_f = OPS_A[0].get("ops") #맨 처음 경기 OPS

for i in OPS_A:
    OPS_growth = OPS_A[i].get("ops") - OPS_f #한 경기 OPS - 맨 처음경기 OPS
    ops_y.append({"year":OPS_A[i].get("year"), "month":OPS_A[i].get("month"), "ops": OPS_growth}) #ops_y 리스트에 추가

print ops_y

#x축은 시간(경기), y축은 OPS 성장률
