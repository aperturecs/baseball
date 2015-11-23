#-*- coding: utf-8 -*-
from hitterGame import HitterGame
from query import Query

def growth(playerId):

    sql = Query()
    queries = sql.quering_select("Select * from HitterGames where playerId="+str(playerId))

    games = []

    def find(year, month):
        temps = []
        for game in games:
            if game.year == year and game.month==month:
                temps.append(game)
        return temps

    for query in queries:
        game = HitterGame(query[1],query[2],query[3],query[4],query[5],query[6],query[7],query[8],query[9],query[10],query[11],query[12],query[13],query[14],query[15],query[16],query[17],query[18],query[19],query[20])
        games.append(game)

    Games = []

    for year in range(2010,2016):
        for month in range(3,11):
            tempGame = {"year":year,"month":month,"OPS":0.0,"H":0,"BB":0,"HBP":0,"AB":0,"HBP":0,"TB":0}
            tempGames = find(year, month)
            for game in tempGames:
                tempGame["H"] += game.H
                tempGame["BB"]+= game.BB
                tempGame["HBP"]+= game.HBP
                tempGame["AB"]+=game.AB
                tempGame["TB"]+= game.H + game.B2*2 + game.B3*3 + game.HR*4
            Games.append(tempGame) # [{"year":year,"month":month,"OPS":0.0,"H":0,"BB":0,"HBP":0,"AB":0,"HBP":0,"TB":0}]
    OPS_A = [] #매월 경기 OPS

    for game in Games:
        try:
            OBP = (game["H"] + game["BB"] + game["HBP"])*1.0 / (game["AB"] + game["BB"] + game["HBP"])*1.0
            OBP = round(OBP,4)
            SLG = game["TB"] / game["AB"]
            OPS = OBP + SLG
            if OPS > 0.0:
                OPS_A.append({"year":game["year"], "month":game["month"], "OPS":OPS}) #계산한 OPS 매월별 집어넣기
        except:
            pass


    OPS_y =[] #OPS 성장률 y값
    OPS_f = OPS_A[0].get("OPS")

    for OPS in OPS_A:
        OPS_growth = OPS["OPS"] - OPS_f #한 경기 OPS - 맨 처음경기 OPS
        y = {"year":OPS["year"],"month":OPS["month"], "growth": OPS_growth}
        OPS_y.append(y) #ops_y 리스트에 추가

    return OPS_y
