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

def stat(playerId):
    sql = Query()

    # 장타율
    SLG_Total = 0.0
    slg_queries = sql.quering_select("Select SLG from HitterProfiles")

    for SLG in slg_queries:
        SLG_Total= SLG_Total + SLG[0]
    SLG_Total = SLG_Total / slg_queries.size()
    player_SLG = sql.quering_select("Select SLG from HitterProfiles where playerId="+str(playerId))
    SLG_Point = player_SLG[0] / SLG_Total * 100
    SLG_Point = round(SLG_Point)

    #출루율
    OBP_Total = 0.0
    obp_query = sql.quering_select("Select OBP from HitterProfiles")
    for OBP in obp_query:
        OBP_Total = OBP_Total + OBP[0]
    OBP_Total = OBP_Total / obp_query.size()
    plyaer_OBP = sql.quering_select("Select OBP from HitterProfiles where playerId="+str(playerId))
    OBP_Point = player_OBP[0] / OBP_Total * 100
    OBP_Point = round(OBP_Point)

    #주루율
    player_SB = sql.quering_select("Select SB from HitterProfiles where playerId="+str(playerId))
    SB_Point = round(player_SB[0])


    #득점율
    RISP_Total = 0.0
    risp_query = sql.quering_select("Select RISP from HitterProfiles")
    for RISP in risp_query:
        RISP_Total = RISP_Total + RISP[0]
    RISP_Total = RISP_Total / risp_query.size()
    player_RISP = sql.quering_select("Select RISP from HitterProfiles where playerId="+str(playerId))
    RISP_Point = round(player_RISP[0] / RISP_Total * 100)

    #수비율
    E_Total = 0.0
    E_query = sql.quering_select("Select G,E from HitterProfiles")
    for G,E in E_query:
        E_Total = E_Total + E/G
    E_Total = E_Total / E_query.size()
    player_E = sql.quering_select("Select G,E from HitterProfiles where playerId="+str(playerId))
    E_Point = round(player_E[0] / E_Total * 100)

    #long : 장타 , hit : 타율, run : 주루율, point : 득점율, defence : 수비율
    result = {"long":SLG_Point, "hit":OBP_Point, "run":SB_Point, "point":RISP_Point, "defence":E_Point}
    return result
