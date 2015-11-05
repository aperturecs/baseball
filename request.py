#-*- coding: utf-8 -*-
import parser

result = []

f = open("result.txt","w")

l = [60288
,79215
,72214
,76290
,76232
,79240
,79231
,75334
,76267
,77248
,62265
,97571
,62929]


for playerId in l:
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
