#-*- coding: utf-8 -*-
class PitcherGame:

    def __init__(self,year,date,sideTeam,position,result,ERA1,TBF,IP,H,HR,BB,HBP,SO,R,ER,ERA2):
        self.type= "Pitcher"
        self.year = year
        self.month = int(date.split(".")[0])
        self.day = int(date.split(".")[1])
        self.sideTeam = sideTeam
        self.postion = position
        if result == "승":
            self.win = True
        else:
            self.win = False
        self.ERA1 = ERA1
        self.TBF = TBF
        self.IP = int(IP.split(" ")[0])
        self.H = H
        self.HR = HR
        self.BB = BB
        self.HBP = HBP
        self.SO = SO
        self.R = R
        self.ER = ER
        self.ERA2 = ERA2
