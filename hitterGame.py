import json
class HitterGame():

    def __init__(self, year, date, sideTeam, AVG1, AB, R, H, B2, B3, HR, RBI, SB, CS, BB, HBP, SO, GDP, AVG2):
        self.type= "Hitter"
        self.year = year
        self.month = int(date.split(".")[0])
        self.day = int(date.split(".")[1])
        self.sideTeam = sideTeam
        self.AVG1 = AVG1
        self.AB = AB
        self.R = R
        self.H = H
        self.B2 = B2
        self.B3 = B3
        self.HR = HR
        self.RBI = RBI
        self.SB = SB
        self.CS = CS
        self.BB = BB
        self.HBP = HBP
        self.SO = SO
        self.GDP = GDP
        self.AVG2 = AVG2
    def addQuery(self):
        sql = "INSERT INTO HitterGames(type, year, month, day , sideTeam, AVG1, AB, R, H, B2, B3, HR, RBI, SB, CS, BB, HBP, SO, GDP, AVG2) VALUES("
        sql += "'" + str(self.type) + "',"
        sql += str(self.year)+","
        sql += str(self.month)+","
        sql += str(self.day)+","
        sql += "'" + str(self.sideTeam) + "',"
        sql += str(self.AVG1)+","
        sql += str(self.AB)+","
        sql += str(self.R)+","
        sql += str(self.H)+","
        sql += str(self.B2)+","
        sql += str(self.B3)+","
        sql += str(self.HR)+","
        sql += str(self.RBI)+","
        sql += str(self.SB)+","
        sql += str(self.CS)+","
        sql += str(self.BB)+","
        sql += str(self.HBP)+","
        sql += str(self.SO)+","
        sql += str(self.GDP)+","
        sql += str(self.AVG2)
        sql += ");"
        return sql
