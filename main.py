#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import pitcherProfileParser
import hitterProfileParser
import hitterGameParser
import pitcherGameParser
import playerParser
# from query import Query
from player import Player
from playerCode import PlayerCode

f = open("sql.txt","w")
codes = PlayerCode()
# query = Query()

count = 1

for code in codes.codes:
    player = playerParser.playerParsing(code)
    if player.type =="Hitter":
        if hitterProfileParser.hitterProfileParsing(player) == None:
            count +=1
            print "에러"
            continue
        hitterGameParser.hitterGameParsing(player)
        # query.quering_add(player.addQuery())
        # query.quering_add(player.profile.addQuery())
        f.write(player.addQuery()+"\n")
        f.write(player.profile.addQuery()+"\n")
        for game in player.hitterGames:
            # query.quering_add(game.addQuery())
            f.write(game.addQuery()+"\n")


    else:
        if pitcherProfileParser.pitcherProfileParsing(player) == None:
            count +=1
            print "에러"
            continue
        pitcherGameParser.pitcherGameParsing(player)
        # query.quering_add(player.addQuery())
        # query.quering_add(player.profile.addQuery())
        f.write(player.addQuery()+"\n")
        f.write(player.profile.addQuery()+"\n")
        for game in player.pitcherGames:
            #query.quering_add(game.addQuery())
            f.write(game.addQuery()+"\n")
    print "["+str(count)+"/"+str(len(codes.codes))+"] 이름 :"+ player.name + " 팀 :"+player.team  +" 타입 :"+player.type
    count +=1
    
