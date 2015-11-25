#-*- coding: utf-8 -*-
from hitterGame import HitterGame
from query import Query

def getpoint(list, point):
    max = 0.0
    min = 100.0
    for data in list:
        if max < data:
            max = data
        if min > data:
            min = data

    lenth = max - min
    size = 100 / lenth

    return round((point - min) * size)

def tupleToList(tup):
    datas = []
    results = []
    if type(tup) == "tuple":
        datas = list(tup)
    else:
        datas = tup
    for data in datas:
        if type(data) == "tuple":
            if len(data) == 1:
                results.appned(data[0])
            else:
                result.appned(list(data))
        else:
            results.append(data)

    if len(results) == 1:
        return results[0]

    return results


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
    slg_queries = sql.quering_select("Select SLG from HitterProfiles")
    all_slg = tupleToList(slg_queries)
    player_SLG = sql.quering_select("Select SLG from HitterProfiles where playerId="+str(playerId))
    player_slg = tupleToList(player_SLG)
    print str(all_slg) + str(player_slg)
    SLG_Point = getpoint(all_slg,player_slg)


    #출루율
    obp_query = sql.quering_select("Select OBP from HitterProfiles")
    all_obp = tupleToList(obp_query)
    player_OBP = sql.quering_select("Select OBP from HitterProfiles where playerId="+str(playerId))
    player_obp = tupleToList(player_OBP)
    OBP_Point = getpoint(all_obp,player_obp)

    #주루율
    sb_query = sql.quering_select("Select OBP from HitterProfiles")
    all_sb= tupleToList(sb_query)
    player_SB = sql.quering_select("Select SB from HitterProfiles where playerId="+str(playerId))
    player_sb = tupleToList(player_SB)
    SB_Point = getpoint(all_sb,player_sb)


    #득점율
    risp_query = sql.quering_select("Select RISP from HitterProfiles")
    all_risp = tupleToList(risp_query)
    risp_query = sql.quering_select("Select RISP from HitterProfiles where playerId="+str(playerId))
    player_risp = tupleToList(risp_query)
    RISP_Point = getpoint(all_risp,player_risp)


    #수비율
    array = []
    E_query = sql.quering_select("Select G,E from HitterProfiles")
    for (G,E) in E_query:
    	array.append(E*1.0 / G*1.0)
    player_E = sql.quering_select("Select G,E from HitterProfiles where playerId="+str(playerId))
    player_e = player_E[0][1]*1.0 / player_E[0][0]*1.0
    E_Point = getpoint(array,player_e)


    #long : 장타 , hit : 타율, run : 주루율, point : 득점율, defence : 수비율
    result = {"long":SLG_Point, "hit":OBP_Point, "run":SB_Point, "point":RISP_Point, "defence":E_Point}
    return result
