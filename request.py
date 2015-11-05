#-*- coding: utf-8 -*-
import parser
from playerCode import PlayerCode
result = []

f = open("result.txt","w")

codes = PlayerCode()

for playerId in codes.codes:
    for year in range(2010,2015):

        print playerId
        datas = parser.htmlParsing(parser.httpRequest(playerId,year))

        if datas == None:
            continue


        player = datas["player"]
        player.playerId = playerId
        # httpRequest(선수ID, 파싱할 연도)

        for game in parser.gameParsing(year,datas["records"]):
            player.games.append(game)
            print game.__dict__
        result.append(player)

parser.playerSave(result)

f.close();
