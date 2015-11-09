#-*- coding: utf-8 -*-
import sys
import parser

reload(sys)
sys.setdefaultencoding('utf-8')

players = parser.fileParser()

for player in players:
    print "이름 :" + player.name + " 팀 :" + player.team + " 경기 수: " + str(len(player.games)) + " 포지션: " + player.position
