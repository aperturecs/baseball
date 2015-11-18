#coding:utf-8
from hitterProfile import HitterProfile
from hitterGame import HitterGame

def find(year, month):
    for game in games:
        if game.year == year and game.month:
            games.append(game)

    return games

Games = []

for year in range(2010,2015):
    for month in range(3,10):
        tempGame = {"year":year,"month":month,"OPS":0.0,"H":0,"BB":0,"HBP":0,"AB":0,"HBP":0,"TB":0})
        tempGames = find(year,month)
        for game in tempGames:
            tempGame["H"] += game.H
            tempGame["BB"]+= game.BB
            tempGame["HBP"]+= game.HBP
            tempGame["AB"]+=game.AB
            tempGame["TB"]+= game.H + game.2B*2 + game.3B*3 + game.HR*4
        Games.appned(tempGame)

OPS_A = [] #매월 경기 OPS


for game in Games:
    OBP = (game.H + game.BB + game.HBP)/(game.AB + game.BB + game.SF + game.HBP)
    SLG = game.TB/game.AB
    OPS = OBP + SLG
    OPS_A.append(OPS)

OPS_y =[] #OPS 성장률 y값
OPS_f = OPS_A[0] #맨 처음 경기 OPS

for OPS_Element in OPS_A:
    OPS_growth = OPS_Element - OPS_f #한 경기 OPS - 맨 처음경기 OPS
    ops_y.append(OPS_growth) #ops_y 리스트에 추가


#x축은 시간(경기), y축은 OPS 성장률
