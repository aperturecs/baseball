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

def getPointArray(list):
    max = 0.0
    min = 100.0
    for data in list:
        if max < data:
            max = data
        if min > data:
            min = data

    lenth = max - min
    size = 100 / lenth

    result = []
    for data in list:
        result.append(round((data - min) * size))
    return result

def tupleToList(tup):
    datas = []
    results = []

    if type(tup) == "tuple":
        datas = list(tup)
    else:
        datas = tup

    for data in datas:
        if len(list(data)) == 1:
            results.append(list(data)[0])
        else:
            results.append(list(data))

    if len(results) == 1:
        return results[0]

    return results

def profile(playerId):
    sql = Query()
    name= tupleToList(sql.quering_select("select name from players where playerId="+str(playerId)))
    image = tupleToList(sql.quering_select("select image from players where playerId="+str(playerId)))
    position = tupleToList(sql.quering_select("select position from players where playerId="+str(playerId)))
    position_detail = tupleToList(sql.quering_select("select position_detail from players where playerId="+str(playerId)))
    team = tupleToList(sql.quering_select("select team from players where playerId="+str(playerId)))

    return {"name":name,"playerId":playerId,"image":image,"postion":position,"position_detail":position_detail,"team":team}

def getPlayerId(name):
    sql = Query()
    playerId= tupleToList(sql.quering_select("select playerId from players where name='"+str(name)+"'"))
    return {"playerId":playerId}

def growth(playerId):
    sql = Query()
    queries = sql.quering_select("select Round(AVG(AVG1),3) from HitterGames where playerId="+str(playerId)+" Group by year,month")
    points = getPointArray(tupleToList(queries))
    queries = tupleToList(sql.quering_select("select year,month from HitterGames where playerId="+str(playerId)+" Group by year,month"))

    return {"date":queries, "points":points}


def stat(playerId):
    sql = Query()

    # 장타율
    slg_queries = sql.quering_select("Select SLG from HitterProfiles")
    all_slg = tupleToList(slg_queries)
    player_SLG = sql.quering_select("Select SLG from HitterProfiles where playerId="+str(playerId))
    player_slg = tupleToList(player_SLG)
    SLG_Point = getpoint(all_slg,player_slg)


    #출루율
    obp_query = sql.quering_select("Select OBP from HitterProfiles")
    all_obp = tupleToList(obp_query)
    player_OBP = sql.quering_select("Select OBP from HitterProfiles where playerId="+str(playerId))
    player_obp = tupleToList(player_OBP)
    OBP_Point = getpoint(all_obp,player_obp)

    #주루율
    sb_query = sql.quering_select("Select SB from HitterProfiles")
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

def simmilar(playerId):
    sql = Query()
    p = tupleToList(sql.quering_select("Select AVG from HitterProfiles where playerId="+str(playerId)))
    players_avg = tupleToList(sql.quering_select("Select playerId from HitterProfiles where (AVG-"+str(p)+")>=0 and playerId!="+str(playerId)+" ORDER BY (AVG-"+str(p)+")"))
    result = []
    result.append(players_avg[0])
    result.append(players_avg[1])
    result.append(players_avg[2])
    return result
