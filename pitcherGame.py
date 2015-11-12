#-*- coding: utf-8 -*-
class PitcherGame:

    def __init__(self,playerId,year,date,sideTeam,position,result,ERA1,TBF,IP,H,HR,BB,HBP,SO,R,ER,ERA2):
        self.playerId = playerId
        self.type= "Pitcher"
        self.year = year
        self.month = int(date.split(".")[0])
        self.day = int(date.split(".")[1])
        self.sideTeam = sideTeam
        self.position = position
        if result == "승":
            self.win = True
        else:
            self.win = False
        self.ERA1 = ERA1
        self.TBF = TBF
        IP = IP.split(" ")[0]
        if len(IP)==3 and IP[1] == "/":
            IP = "1"
        self.IP = int(IP)
        self.H = H
        self.HR = HR
        self.BB = BB
        self.HBP = HBP
        self.SO = SO
        self.R = R
        self.ER = ER
        self.ERA2 = ERA2

    def addQuery(self):
        sql = "INSERT INTO PitcherGames (playerId,type,year,month,day,sideTeam,position,win,ERA1,TBF,IP,H,HR,BB,HBP,SO,R,ER,ERA2) VALUES("
        sql += str(self.playerId) + ","
        sql += "'"+str(self.type) + "',"
        sql += str(self.year) + ","
        sql += str(self.month) + ","
        sql += str(self.day) + ","
        sql += "'"+str(self.sideTeam) + "',"
        sql += "'"+str(self.position) + "',"
        sql += str(self.win) + ","
        sql += str(self.ERA1) + ","
        sql += str(self.TBF) + ","
        sql += str(self.IP) + ","
        sql += str(self.H) + ","
        sql += str(self.HR) + ","
        sql += str(self.BB) + ","
        sql += str(self.HBP) + ","
        sql += str(self.SO) + ","
        sql += str(self.R) + ","
        sql += str(self.ER) + ","
        sql += str(self.ERA2)
        sql += ");"
        return sql
