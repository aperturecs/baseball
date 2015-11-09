#-*- coding: utf-8 -*-
import parser
import sys
import traceback
import time
from playerCode import PlayerCode
import ErrorCode
reload(sys)
sys.setdefaultencoding('utf-8')

result = []
codes = PlayerCode()

f = open("result.txt","w")

errorList = []
start_time = 0
count = 1


for playerId in codes.codes:

    try:
        start_time = time.time()
        request = parser.httpRequest(playerId,2014,"Hitter")
        player = parser.playerParsing(playerId,request)

        if player.position == "투수":
            player.pitcherGames = parser.parsing(player,"Pitcher")
        player.games = parser.parsing(player,"Hitter")

        result.append(player)

        parser.playerSave(f,player)
        print "------------------------------"
        print "선수이름 :"+player.name
        print "선수 포지션 :"+player.position
        print "선수 팀 :"+player.team
        print "타자 출장 :"+str(len(player.games))
        print "투수 출장 :"+str(len(player.pitcherGames))
        print "크롤링 소요 시간 :"+str(round(time.time()-start_time,2))+"초"
        print "진행현황 : "+str(count)+"/"+ str(len(codes.codes))
        print "-------------------------------"
        count +=1

    except:
        print "*******************************"
        print "선수 Id :"+str(playerId) +"에러 발생"
        print "*******************************"
        errorList.append(playerId)
        traceback.print_exc()
        pass
f.close()

print "*********파싱완료*********"
print "에러 리스트 :"+ str(errorList)
