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

codes = PlayerCode()
# query = Query()

for code in codes.codes:
    player = playerParser.playerParsing(code)
    print player.addQuery()
    if player.type =="Hitter":
        hitterProfileParser.hitterProfileParsing(player)
        hitterGameParser.hitterGameParsing(player)
        # query.quering_add(player.addQuery())
        # query.quering_add(player.profile.addQuery())
        print player.profile.addQuery()
        for game in player.hitterGames:
            # query.quering_add(game.addQuery())
             print game.addQuery()

    else:
        pitcherProfileParser.pitcherProfileParsing(player)
        pitcherGameParser.pitcherGameParsing(player)
        # query.quering_add(player.addQuery())
        # query.quering_add(player.profile.addQuery())
        print player.profile.addQuery()
        for game in player.pitcherGames:
            #query.quering_add(game.addQuery())
             print game.addQuery()
    print "이름 :"+ player.name + " 팀 :"+player.team  +" 타입 :"+player.type
