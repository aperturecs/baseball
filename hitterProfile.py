class HitterProfile:
    def __init__(self,playerId, Team, AVG, G, PA, AB, R, H, B2, B3, HR, TB, RBI, SB, CS, SAC, SF, BB, IBB, HBP, SO, GDP, SLG, OBP, E, SBP, MH, OPS, RISP, PHBA):
        self.playerId = playerId
        self.team = Team
        self.AVG = AVG
        self.G = G
        self.PA = PA
        self.AB = AB
        self.R = R
        self.H = H
        self.B2 = B2
        self.B3 = B3
        self.HR = HR
        self.TB = TB
        self.RBI = RBI
        self.SB = SB
        self.CS = CS
        self.SAC = SAC
        self.SF = SF
        self.BB = BB
        self.IBB = IBB
        self.HBP = HBP
        self.SO = SO
        self.GDP = GDP
        self.SLG = SLG
        self.OBP = OBP
        self.E = E
        self.SBP = SBP
        self.MH = MH
        self.OPS = OPS
        self.RISP = RISP
        self.PHBA = PHBA

    def addQuery(self):
        sql = "INSERT INTO HitterProfiles (playerId, Team, AVG, G, PA, AB, R, H, B2, B3, HR, TB, RBI, SB, CS, SAC, SF, BB, IBB, HBP, SO, GDP, SLG, OBP, E, SBP, MH, OPS, RISP, PHBA) VALUES("
        sql += str(self.playerId)+","
        sql += "'" + str(self.team)+"',"
        sql += str(self.AVG)+","
        sql += str(self.G)+","
        sql += str(self.PA)+","
        sql += str(self.AB)+","
        sql += str(self.R)+","
        sql += str(self.H)+","
        sql += str(self.B2)+","
        sql += str(self.B3)+","
        sql += str(self.HR)+","
        sql += str(self.TB)+","
        sql += str(self.RBI)+","
        sql += str(self.SB)+","
        sql += str(self.CS)+","
        sql += str(self.SAC)+","
        sql += str(self.SF)+","
        sql += str(self.BB)+","
        sql += str(self.IBB)+","
        sql += str(self.HBP)+","
        sql += str(self.SO)+","
        sql += str(self.GDP)+","
        sql += str(self.SLG)+","
        sql += str(self.OBP)+","
        sql += str(self.E)+","
        sql += str(self.SBP)+","
        sql += str(self.MH)+","
        sql += str(self.OPS)+","
        sql += str(self.RISP)+","
        sql += str(self.PHBA)
        sql += ");"
        return sql
        