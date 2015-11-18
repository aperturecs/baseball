# -*- coding: utf-8 -*-
from query import Query

class ApiManager:

    def __init__(self):
        self.query = Query()

    def getPlayerInfo(self,name):

        #    {
        #   "name":"김준성",
        #   "playerID":333333,
        #   "team":"두산",
        #   "position":"내야수",
        #   "position_detail":"우투좌타",
        #   "back_number":13,
        #   "player_image":"http://.../.jpg"
        #   }

        que = "Select (playerId, team, position, position_detail, back_number, image) from players where name ='"+name+"';"
        sql = self.query.quering_select(que)
        data = {"name":name,"playerId":sql[0],"team":sql[1],"position":sql[2],"position_detail":sql[3],"back_number":sql[4],"image":sql[5]}
        return data

    def getOPS(self,playerId):

        que 
