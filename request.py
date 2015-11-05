#-*- coding: utf-8 -*-
import parser

playerId = 74339
year = 2015
for year in range(2010,2015):
    datas = parser.htmlParsing(parser.httpRequest(playerId,year))
    # httpRequest(선수ID, 파싱할 연도)
    for game in parser.gameParsing(year,datas):
        print game.__dict__
