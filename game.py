import json
class Game(object):

    def __init__(self, year, date, sideTeam, AVG1, AB, R, H, B2, B3, HR, RBI, SB, CS, BB, HBP, SO, GDP, AVG2):
        self.type= "Hitter"
        self.year = year
        self.date = date
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
<<<<<<< Updated upstream
        self.AVG2 = AVG2
=======
    def intodata(year, date, sideTeam, AB, R, H, B2, B3, HR, RBI, SB, CS, BB, HBP, SO, GDP):
>>>>>>> Stashed changes
