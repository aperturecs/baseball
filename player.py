class Player(object):

    def __init__(self, playerId, name, team, postion, position_detail, img_url):
        self.type = "Hitter"
        self.image = img_url
        self.name = name
        self.playerId = playerId
        self.team = team
        self.position = postion
        self.position_detail = position_detail
        self.hitterGames = []
        self.pitcherGames =[]
        self.profile = None;

    def addQuery(self):
        sql = "INSERT INTO players (type, playerId, name, team, position, position_detail, image) VALUES("
        sql += "'" + str(self.type) +"',"
        sql += str(self.playerId) +","
        sql += "'" + str(self.name) +"',"
        sql += "'" + str(self.team) +"',"
        sql += "'" + str(self.position) +"',"
        sql += "'" + str(self.position_detail) +"',"
        sql += "'" + str(self.image) +"'"
        sql += ");"
        return sql
