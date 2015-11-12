class PitcherProfile:

    def __init__(self, playerId ,Team, ERA, G, CG, SHO, W, L, SV, HLD, WPCT, TBF, NP, IP, H, B2, B3, HR, SAC, SF, BB, IBB, SO, WP, BK, R, ER, BSV, WHIP, AVG, QS):
        self.playerId = playerId
        self.Team = Team
        self.ERA = ERA
        self.G = G
        self.CG = CG
        self.SHO = SHO
        self.W = W
        self.L = L
        self.SV = SV
        self.HLD = HLD
        self.WPCT = WPCT
        self.TBF = TBF
        self.NP = NP
        self.IP = int(IP.split(" ")[0])
        self.H = H
        self.B2 = B2
        self.B3 = B3
        self.HR = HR
        self.SAC = SAC
        self.SF = SF
        self.BB = BB
        self.IBB = IBB
        self.SO = SO
        self.WP = WP
        self.BK = BK
        self.R = R
        self.ER = ER
        self.BSV = BSV
        self.WHIP = WHIP
        self.AVG = AVG
        self.QS = QS

    def addQuery(self):
        sql = "INSERT INTO PitcherProfiles (playerId ,Team, ERA, G, CG, SHO, W, L, SV, HLD, WPCT, TBF, NP, IP, H, B2, B3, HR, SAC, SF, BB, IBB, SO, WP, BK, R, ER, BSV, WHIP, AVG, QS) VALUES("
        sql += str(self.playerId)+","
        sql += "'" + self.Team +"',"
        sql += str(self.ERA)+","
        sql += str(self.G)+","
        sql += str(self.CG)+","
        sql += str(self.SHO)+","
        sql += str(self.W)+","
        sql += str(self.L)+","
        sql += str(self.SV)+","
        sql += str(self.HLD)+","
        sql += str(self.WPCT)+","
        sql += str(self.TBF)+","
        sql += str(self.NP)+","
        sql += str(self.IP)+","
        sql += str(self.H)+","
        sql += str(self.B2)+","
        sql += str(self.B3)+","
        sql += str(self.HR)+","
        sql += str(self.SAC)+","
        sql += str(self.SF)+","
        sql += str(self.BB)+","
        sql += str(self.IBB)+","
        sql += str(self.SO)+","
        sql += str(self.WP)+","
        sql += str(self.BK)+","
        sql += str(self.R)+","
        sql += str(self.ER)+","
        sql += str(self.BSV)+","
        sql += str(self.WHIP)+","
        sql += str(self.AVG)+","
        sql += str(self.QS)
        sql += ");"
        return sql

        